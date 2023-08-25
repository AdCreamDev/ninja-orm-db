from django.shortcuts import render

from ninja import Query, Router, Schema
router = Router(tags=["home"])


# Create your views here.
@router.get("/hi")
def index(request):
    return "home index"


@router.get("/")
def index(request):
    return render(request, ".\home\index.html")

