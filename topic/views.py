from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from user.models import User
from datetime import datetime
from rolepermissions.roles import get_user_roles
from topic.models import TopicRecord, Topic2User, Annex, Annex2Topic2User
from topic.forms import TopicRecordForm, Topic2UserForm
from django.http import HttpResponse
from utils.fdfs.storage import FDFSStorage
from django.conf import settings
import os


# /topic/
# 获取所有题目
@login_required
def show_all_topic(request):
    current_user = request.user
    # 通过查询TopicRecord表返回所有题目
    result = TopicRecord.objects.all()
    try:
        role = get_user_roles(current_user)[0].get_cls_name()
    except IndexError:
        role = ''
    context = {
        'result': result,
        'name': current_user.name,
        'role': role
    }
    return render(request, "index.html", context)


# /topic/index/
# 获取当前用户id的所有题目
@login_required
def show_index(request):
    # 通过session获取当前登录用户对象
    current_user = request.user
    # 获取用户id
    current_user_id = current_user.id
    print(current_user.username)
    # 通过用户id查询Topic2User表，获取到当前用户的所有题目
    result_list = Topic2User.objects.filter(user_id=current_user_id)

    topic_list = list()
    for topic in result_list:
        topic_obj = TopicRecord.objects.get(id=topic.topic_id_id)
        topic_list.append(topic_obj)

    try:
        # 获取用户角色
        role = get_user_roles(current_user)[0].get_cls_name()
    except IndexError:
        role = ''

    # 创建context字典，返回结果
    context = {
        'result': topic_list,
        'name': current_user.name,
        'role': role
    }
    return render(request, "test_show_index.html", context)


# /topic/create/
# 创建题目（role==teacher）
@login_required
def test_create_topic(request):
    # 获取当前用户对象
    current_user = request.user
    try:
        # 获取用户对应角色
        role = get_user_roles(current_user)[0].get_cls_name()
    except IndexError:
        role = ''
    # 获得form，并写入数据库
    if request.method == 'POST':
        form = TopicRecordForm(request.POST)
        file = request.FILES.get("file")
        temp_file = "%s/%s" % (settings.MEDIA_ROOT, file.name)
        with open(temp_file, 'wb') as upload_files:
            for chunk in file.chunks():
                upload_files.write(chunk)

        # 将文件写入临时文件

        file_path = os.path.abspath(temp_file)
        print(file_path)
        fdfs_storage = FDFSStorage()
        remote_file_id = fdfs_storage.upload(file_path)[1]

        # file = TopicRecordForm(request.FILES.get("file"))
        # if form.is_valid():
        #     form.save()
        #     if file is None:
        #         return HttpResponse("没有上传文件")
        #     else:
        #         with open("media/", "wb+") as f:
        #             for chunk in file.chunks():
        #                 f.write(chunk)
        #                 file.save()
        if form.is_valid():
            form.save()
        title = form.clean().get("title")
        topic_id = TopicRecord.objects.get(title=title)
        user = request.user
        user_id = user

        Topic2User.objects.create(topic_id=topic_id, user_id=user_id)
        Annex.objects.create(file=remote_file_id)
        annex_id = Annex.objects.get(file=remote_file_id)
        Annex2Topic2User.objects.create(annex_id=annex_id, topic_id=topic_id, user_id=user_id)

        return redirect(reverse('topic:show_my_topic'))

    context = {
        'name': current_user.name,
        'role': role
    }
    return render(request, "test_create_topic.html", context)


# /topic/show-(\d+)
# 查看题目详情
@login_required
def topic_detail(request, topic_id):
    if request.method == 'GET':
        # 获取当前topic_id对应的题目对象
        obj = TopicRecord.objects.get(id=topic_id)
        # if not obj:
        #     return HttpResponse('已被学生选择或教秘确认完成的题目无法被编辑')

        teacher_id = Topic2User.objects.filter(topic_id=topic_id)
        print(teacher_id)
        title = obj.title
        # 通过Topic2User表获取teacher_id
        teacher = Topic2User.objects.get(topic_id=topic_id)
        teacher = teacher.user_id
        # 通过teacher_id获取教师姓名
        teacher = User.objects.get(username=teacher)
        teacher = teacher.name
        chosen_num = obj.chosen_num
        limit_num = obj.limit_num
        release_time = obj.release_time
        last_edit_time = obj.last_edit_time
        detail = obj.detail
        context = {
            "title": title,
            "teacher": teacher,
            "chosen_num": chosen_num,
            "limit_num": limit_num,
            "release_time": release_time,
            "last_edit_time": last_edit_time,
            "detail": detail
        }
        return render(request, "topic_detail.html", context)


# /topic/delete-(\d+)
# 查看题目详情
@login_required
def delete_topic(request, topic_id):
    TopicRecord.objects.get(id=topic_id).delete()
    return redirect(reverse("topic:show_my_topic"))


# /upload
# 上传文件
@login_required
def upload_file(request):
    if request.method == 'POST':
        print(request.user)
        file = request.FILES.get("file")
        if file is None:
            return HttpResponse("没有上传文件")
        else:
            file.save()
            with open("media/%s" % file.name, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)
            return HttpResponse("Over")
    else:
        return render(request, "upload_file.html")
