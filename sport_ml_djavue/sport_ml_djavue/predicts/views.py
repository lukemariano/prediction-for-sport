# coding: utf-8
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import log_svc, predict_svc


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }

    return d


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Obtém as informações de registro enviadas pelo front-end
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Salva as informações de registro do usuário no banco de dados
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Redireciona o usuário para a página de login
        return redirect('/')

    return redirect('/register')


@ajax_login_required
def list_predicts(request):
    predicts = predict_svc.list_predicts()
    return JsonResponse({"predicts": predicts})


@csrf_exempt
@ajax_login_required
def add_predict(request):
    predict = predict_svc.add_predict(request.POST)
    return JsonResponse(predict)


