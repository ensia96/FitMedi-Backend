from django.views import View
from django.http import HttpResponse, JsonResponse


class UserAuthView(View):
    def get(self, request):
        return JsonResponse({"message": "for_test haha"}, status=200)

