from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from libs.random.random import Random

# Create your views here.
class Hoge(View):
    
    @require_GET
    def get(self):
        data = {
            "hoge": "piyo",
            "int": Random.get_random_int(),
        }

        return JsonResponse(data)
