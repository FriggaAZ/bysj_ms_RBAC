from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import User
from rolepermissions.roles import get_user_roles
from topic.models import TopicRecord, Topic2User


# Create your views here.

@login_required
def show_all_topic(request):
    result = Topic2User.objects.all()
    return render(request, "index.html", {"result": result})


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
    return render(request, "test_create_topic.html")
