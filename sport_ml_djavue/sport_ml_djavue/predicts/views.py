# coding: utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import predict_svc


@csrf_exempt
@ajax_login_required
def add_predict(request):
    predict = predict_svc.add_predict(request.POST)
    return JsonResponse(predict)


@ajax_login_required
def list_predicts(request):
    predicts = predict_svc.list_predicts()
    return JsonResponse({"predicts": predicts})
