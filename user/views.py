import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import User


class UserAuthView(View):
    def get(self, request):
        return JsonResponse({"message": "for_test haha"}, status=200)

    def post(self, request):
        data = json.loads(request.body)
        print(data["user"])
        print(data["password"])
        User.objects.get_or_create(user=data["user"], password=data["password"])
        return JsonResponse(data, status=200)
