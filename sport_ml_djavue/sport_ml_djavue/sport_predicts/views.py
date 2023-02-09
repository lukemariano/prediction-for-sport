# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc


@csrf_exempt
@ajax_login_required
def add_todo(request):
    predict = todo_svc.add_todo(request.POST)
    return JsonResponse(predict)


@ajax_login_required
def list_todos(request):
    predicts = todo_svc.list_todos()
    return JsonResponse({"predicts": predicts})
