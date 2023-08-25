from django.shortcuts import render

from ninja import Query, Router, Schema
router = Router(tags=["auth"])

@router.get("/login")
def get_login(request):
    return render(request, ".\\auth\login.html")

@router.get("/signup")
def get_signup(request):
    return render(request, ".\\auth\signup.html")


@router.post("/signup")
def post_signup(request):
    return render(request, ".\\auth\signup.html")
   



