from django.shortcuts import render, redirect
from django.contrib import messages as django_messages
from .models import Project, Skill, Message


def home(request):
    context = {
        "projects": Project.objects.all(),
        "skills": Skill.objects.all(),
    }
    return render(request, "portfolio/home.html", context)


def about(request):
    context = {
        "about_text": (
            "I'm a Computer Science undergrad specializing in Data Science at "
            "Taylor's University, building ML pipelines and full-stack apps."
        )
    }
    return render(request, "portfolio/about.html", context)


def contact(request):
    if request.method == "POST":
        Message.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            content=request.POST.get("content"),
        )
        django_messages.success(request, "Message sent!")
        return redirect("home")
    return redirect("home")
