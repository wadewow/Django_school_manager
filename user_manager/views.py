from django.shortcuts import render, redirect
from user_manager import models
from django import views
from django.utils.decorators import method_decorator
# Create your views here.


def outer(func):
    def inner(request, *args, **kwargs):
        print('当前URL：%s' % request.get_raw_uri())
        print('请求方法：%s' % request.method)
        return func(request, *args, **kwargs)
    return inner


def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return inner


class Login(views.View):

    def dispatch(self, request, *args, **kwargs):
        print('准备执行函数')
        ret = super(Login, self).dispatch(request, *args, **kwargs)
        print('函数执行完毕')
        return ret

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        c_username = request.POST.get('username')
        c_password = request.POST.get('password')
        c = models.Administrator.objects.filter(username = c_username, password = c_password).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = c_username
            rep = redirect('/index/')
            return rep
        else:
            error = '用户或密码错误'
            return render(request, 'login.html', locals())


class Index(views.View):

    @method_decorator(auth)
    def get(self, request):
        username = request.session.get('username')
        return render(request, 'index.html', locals())


class Class(views.View):

    @method_decorator(auth)
    def get(self, request):
        username = request.session.get('username')
        # 获取所有的班级列表
        class_list = models.Classes.objects.all()
        return render(request, 'class.html', locals())


class Student(views.View):

    @method_decorator(auth)
    def get(self, request):
        username = request.session.get('username')
        return render(request, 'student.html', locals())


class Teacher(views.View):

    @method_decorator(auth)
    def get(self, request):
        username = request.session.get('username')
        return render(request, 'teacher.html', locals())
