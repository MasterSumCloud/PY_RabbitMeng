# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
import json
from .models import User
import requests


def regist(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        username = parames['username']
        password = parames['password']
        if username is not None and password is not None:
            if User.objects.filter(username=username):
                return HttpResponse(json.dumps({'state': False, 'msg': '账号已存在'}), content_type='application/json')
            else:
                User.objects.create(username=username, password=password)
                return HttpResponse(json.dumps({'state': True, 'msg': '注册成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '注册信息不能为空'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def changepass(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        username = parames['username']
        password = parames['password']
        newPassword = parames['newPassword']

        user = User.objects.filter(username=username, password=password)

        if user:
            User.objects.update(username=username, password=newPassword)
            return HttpResponse(json.dumps({'state': True, 'msg': '修改成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '账号或者密码错误'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def login(request):
    if request.method == 'POST':
        # username = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        parames = json.loads(request.body)
        username = parames['username']
        password = parames['password']
        user = User.objects.filter(username=username, password=password)
        if user:
            return HttpResponse(json.dumps({'state': True, 'msg': '登陆成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '账号或者密码错误'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def clans(request):
    if request.method == 'POST':

        parames = json.loads(request.body)
        tag = parames['tag'].replace('#', '%23')
        url = 'https://api.clashofclans.com/v1/clans/' + tag
        res = requests.get(url, None, headers=getheads())
        if res.status_code == 200:
            return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': res.json()}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '请求失败'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def players(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        tag = parames['tag'].replace('#', '%23')
        url = 'https://api.clashofclans.com/v1/players/' + tag
        res = requests.get(url, None, headers=getheads())
        if res.status_code == 200:
            return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': res.json()}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '请求失败'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def currentwar(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        tag = parames['tag'].replace('#', '%23')
        url = 'https://api.clashofclans.com/v1/clans/' + tag + '/currentwar'
        res = requests.get(url, None, headers=getheads())
        if res.status_code == 200:
            return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': res.json()}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '请求失败'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def getheads():
    headers = {
        'charset': 'UTF-8',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQyYzNmNzRjLWM2Y2QtNDM4Ny1hOTAwLTE3MWY5ZDc1NzA1ZiIsImlhdCI6MTUzMDY4MjA2MSwic3ViIjoiZGV2ZWxvcGVyL2ZjMDMxNDMzLWEzNDQtZmY3NS05OGUwLTNlZjlkNmJjZjljYSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExNi4yMzEuMTU5LjEwOCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.D4VZAid5jrPZOY-Y1FIxCqnShRpXdoxX4UsZuLzuh-aYzR8mg3ILl5ChUtAMVRJxAGFUmiDwLwVk_GtTVGP4Kg',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    return headers
