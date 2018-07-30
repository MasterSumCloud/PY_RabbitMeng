from django.shortcuts import render
from .models import warlist
from django.http import HttpResponse
import json
from django.core import serializers


def warstarttime(request):
    balcklist = warlist.objects.all()
    jsonlist = json.loads(serializers.serialize('json', balcklist))
    if request.method == 'POST':

        return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': jsonlist}),
                            content_type='application/json')
    elif request.method == 'GET':
        return HttpResponse(json.dumps({'state': True, 'msg': '请求成功', 'data': jsonlist}),
                            content_type='application/json')
    else:
        return HttpResponse(json.dumps({'state': False, 'msg': '错误未知'}), content_type='application/json')
