from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View
from user.models import User
from django.contrib.auth import authenticate, login, logout
from rolepermissions.roles import assign_role

# Create your views here.


# /register/
class RegisterView(View):

    def get(self, request):
        '''显示注册页面'''
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('registerName', None)
        username = request.POST.get('registerUsername', None)
        password = request.POST.get('registerPassword', None)
        school = request.POST.get('registerSchool', None)
        department = request.POST.get('registerDepartment', None)
        email = request.POST.get('registerEmail', None)

        # email = request.POST.get('registerEmail', None)
        print(name)
        print(username)
        print(password)
        print(school)
        print(department)
        print(email)

        if not all([username, password]):
            print("数据不完整")

        user = User.objects.create_user(
            name=name,
            username=username,
            password=password,
            school=school,
            department=department,
            email=email
        )
        user.save()
        # 默认角色为学生
        assign_role(user, 'student')
        return redirect(reverse('login'))


# /login/
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('userName', None)
        password = request.POST.get('passWord', None)
        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse('topic:show_all_topic'))
            response = redirect(next_url)
            return response
        else:
            return render(request, 'login.html')

        # try:
        #     user = User.objects.get(username=username)
        #     if user.password == password:
        #         if has_role(user, ['teacher']):
        #             # return HttpResponse("Login Success, You are Teacher")
        #             return render(request, 'test_show_index.html')
        #         elif has_role(user, 'student'):
        #             return HttpResponse("Login Success, You are Student")
        #         elif has_role(user, 'systemadmin'):
        #             return HttpResponse("Login Success, You are SystemAdmin")
        #     else:
        #         return HttpResponse("Login Failed")
        #
        # except Exception:
        #     print("没有该用户")
        # return redirect(reverse('login'))


class LogoutView(View):
    '''退出登录'''

    def get(self, request):
        '''退出登录'''
        # 清除用户session信息
        logout(request)
        # 跳转到首页
        return redirect(reverse('login'))
