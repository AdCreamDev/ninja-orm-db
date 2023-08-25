from django.shortcuts import render

from ninja import Query, Router, Schema
router = Router(tags=["home"])

# Create your views here.
@router.get("/index")
def index(request1):
    return "media index"

@router.get("/media")
def selectMedia(request):
    return "get media"

@router.post("/media")
def insertMedia(request):
    return "post media"

@router.put("/media")
def updateMedia(request):
    return "put media"
