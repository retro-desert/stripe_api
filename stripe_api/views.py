import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import stripe_api.stripe_backend as stripe_backend
from stripe_api.models import Item


@csrf_exempt
def buy(_request, pk):
    if _request.method == "GET":
        stripe = stripe_backend.Stripe()
        request_prod = stripe.product_create(_name=Item.objects.filter().all()[pk].name,
                                             _amount=Item.objects.filter().all()[pk].price,
                                             _description=Item.objects.filter().all()[pk].description)
        price_id = request_prod["default_price"]
        request_session = stripe.session_create(_price_id=price_id, _quantity=1)

        return JsonResponse({'session_id': request_session["id"]})

    else:
        return HttpResponse("")


def info(_request, pk):
    if _request.method == "GET":
        form = {
            "pk": pk,
            "name": Item.objects.filter()[pk].name,
            "price": Item.objects.filter()[pk].price / 100,
            "description": Item.objects.filter()[pk].description,
            "apiKey": os.getenv("stripe_publicKey")
        }
        return render(_request, "main/index.html", form)

    else:
        return HttpResponse("")


if __name__ == "__main__":
    pass
