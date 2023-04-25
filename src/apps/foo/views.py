from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from libs.random.random import Random

# Create your views here.
class Foo(View):
    
    @require_GET
    def get(self):
        data = {
            "foo": "bar",
            "int": Random.get_random_int(),
        }

        return JsonResponse(data)
