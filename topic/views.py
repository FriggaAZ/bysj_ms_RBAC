from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from user.models import User
from datetime import datetime
from rolepermissions.roles import get_user_roles
from topic.models import TopicRecord, Topic2User
from topic.forms import TopicRecordForm, Topic2UserForm
from django.http import HttpResponse


# Create your views here.

@login_required
def show_all_topic(request):
    current_user = request.user
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


@login_required
def show_index(request):
    current_user = request.user
    current_user_id = current_user.id
    print(current_user.username)
    result = Topic2User.objects.filter(user_id=current_user_id)

    try:
        role = get_user_roles(current_user)[0].get_cls_name()
    except IndexError:
        role = ''
    context = {
        'result': result,
        'name': current_user.name,
        'role': role
    }
    return render(request, "test_show_index.html", context)


@login_required
def test_create_topic(request):
    current_user = request.user
    try:
        role = get_user_roles(current_user)[0].get_cls_name()
    except IndexError:
        role = ''

    if request.method == 'POST':
        form = TopicRecordForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.clean().get("title")
            topic_id = TopicRecord.objects.get(title=title)
            user = request.user
            user_id = user

            Topic2User.objects.create(topic_id=topic_id, user_id=user_id)

            return redirect(reverse('topic:show_my_topic'))

    context = {
        'name': current_user.name,
        'role': role
    }
    return render(request, "test_create_topic.html", context)


@login_required
def topic_detail(request, topic_id):
    if request.method == 'GET':
        obj = TopicRecord.objects.get(id=topic_id, status=1)
        if not obj:
            return HttpResponse('已被学生选择或确认完成的题目无法被编辑')

        teacher_id = Topic2User.objects.filter(topic_id=topic_id)
        print(teacher_id)
        title = obj.title
        teacher = Topic2User.objects.get(topic_id=topic_id)
        teacher = teacher.user_id
        teacher = User.objects.get(username=teacher)
        teacher = teacher.name
        print("教师id：", teacher)

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
