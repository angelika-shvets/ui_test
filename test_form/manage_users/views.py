from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse
from .user_service import UserService
from collections import OrderedDict


def index(request):
    return render(request, 'manage_users/index.html')

def get_users(request):

    filter_details = _get_filter_details_from_request(request)
    user_service = UserService()
    result = user_service.get_by_filters(filter_details)

    return JsonResponse(result)


def _get_filter_details_from_request(request):
    filter_details = OrderedDict()

    for key, value in request.GET.iteritems():
        filter_details[key] = value

    return filter_details


