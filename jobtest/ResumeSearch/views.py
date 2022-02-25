from django.shortcuts import render, redirect
from django.db import models
from django import forms
from . import models
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings
from django.core.mail import send_mail as sm
app_name = "ResumeSearch"
from django.contrib.auth.decorators import login_required

import datetime
from . models import user, industry, skill, job

from .forms import UserForm, RegisterForm
import hashlib
from itsdangerous import SignatureExpired
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from django.urls import reverse
from django.core import serializers



def hash_code(s, salt='ResumeSearch'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()




def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)

        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:   # 确保用户名和密码都不为空
                username = username.strip()
                # 用户名字符合法性验证
                # 密码长度验证
                # 更多的其它验证.....
                try:
                    user = models.user.objects.get(name=username)

                    if user.password == hash_code(password):
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect(reverse('index'))
                        #return render(request, "index.html", {'username':username})
                    else:
                        message = "Password incorrect !"
                except:
                    message = 'user not exit'
        #return render(request, 'index.html')

    login_form = UserForm
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.user.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())

                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.user.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面

    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def test_ajax(request):

    # res = {"code": 101, "msg": "请求无效"}
    # # 判断是否为ajax请求, 不是返回请求无效
    # if request.is_ajax():
    #     try:
    #         res["code"] = 100
    #         res["msg"] = '请求成功'
    #     except Exception:
    #         res["msg"] = '请求无效'
    #return HttpResponse("res")




    if request.method == 'POST':
        Job = request.POST.get("job")
        Mainjob = request.POST.get("mainjob")
        Input = request.POST.get("input")
        text='this is text'
        print(Mainjob.split('/'))


        #link = request.get_full_path()
        #print(link)
        #job = request.GET.get('job', '')

        #mainjob = request.GET.get('mainjob','')
        #city=request.GET.get('city','')
        print("This is Job："+Job)
        print("This is Mainjob:" +Mainjob)
        print("This is input:" + Input)

        message={}

        jobs = job.objects.filter(title__icontains=Input)


        data = serializers.serialize("json", jobs)
        jsonjobs = {'jobs': data}
        #jobs = job.objects.filter(title__icontains=keyword, location__icontains=city)

        return JsonResponse(jsonjobs)



def index(request):
    #if request.session.get('is_login', None):
    jobs = job.objects.all()
    return render(request, 'index.html', {'jobs': jobs, "register": "注册", "login": "登入"})
    #else:
    #return render(request, 'index.html')

def detail(request, slug):
    jobs = job.objects.get(slug=slug)
    return render(request, 'details.html', {'jobs': jobs})



def search_job(request):

    if request.is_ajax():
        #link = request.get_full_path()
        #print(link)
        job = request.POST.get('job', '')
        mainjob = request.POST.get('mainjob', '')
        input = request.POST.get('input', '')
        #city=request.GET.get('city','')
        print(job)
        print(mainjob)
        print(input)


        jobs = job.objects.filter(title__icontains=job)
        #jobs = job.objects.filter(title__icontains=keyword, location__icontains=city)

        return render(request, 'index.html', {'jobs': jobs})
