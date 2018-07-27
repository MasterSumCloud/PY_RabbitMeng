from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import BlackList
from django.core import serializers


def addblaclk(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        clanname = parames['clanname']
        clantag = parames['clantag']
        if clantag is not None:
            if BlackList.objects.filter(clantag=clantag):
                return HttpResponse(json.dumps({'state': False, 'msg': '已登记'}), content_type='application/json')
            else:
                BlackList.objects.create(clanname=clanname, clantag=clantag)
                return HttpResponse(json.dumps({'state': True, 'msg': '登记成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '注册信息不能为空'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def deletebalck(request):
    if request.method == 'POST':
        parames = json.loads(request.body)
        clantag = parames['clantag']
        success = BlackList.objects.filter(clantag=clantag).delete()
        if success:
            return HttpResponse(json.dumps({'state': True, 'msg': '删除成功'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'state': False, 'msg': '删除失败'}), content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': False, 'msg': '不允许GET请求'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')


def getblack(request):
    balcklist = BlackList.objects.all()
    jsonlist = json.loads(serializers.serialize('json', balcklist))
    if request.method == 'POST':

        return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': jsonlist}),
                            content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': jsonlist}),
                            content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')
