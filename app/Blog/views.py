from django.shortcuts import render, redirect
from Blog.forms import AddPostForm, SignUpForm, UpdateProfileForm
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from Blog.models import Posts, User
from django.views.generic import View
from app.settings import LOGIN_REDIRECT_URL as lru


def signuppage(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "Blog/signup.html", {"form": form})


@login_required
def updateprofile(request):
    user = request.user
    form = UpdateProfileForm(instance=user)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "Blog/updateProfile.html", {"form": form})


@login_required
def updatepassword(request):
    user = request.user
    form = PasswordChangeForm(user)

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect("home")

    return render(request, "Blog/updatePassword.html", {"form": form})


@login_required
def home(request):
    posts = Posts.objects.exclude(writen_by=request.user)
    return render(request, "Blog/home.html", {"posts": posts})


@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    return render(request, "Blog/profile.html", {"user": user})


@login_required
def myPosts(request):
    posts = Posts.objects.filter(writen_by=request.user)
    return render(request, "Blog/MyPosts.html", {"posts": posts})


@login_required
def logoutpage(request):
    logout(request)
    return redirect("login")


@login_required
def addPost(request):
    form = AddPostForm()
    message = ""
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writen_by = request.user
            post.save()
            message = "Post added successfully"

    return render(request, "Blog/AddPost.html", {"form": form, "message": message})


@login_required
def updatePost(request, id):
    post = Posts.objects.get(id=id)

    if request.method == "POST":
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            post.writen_by = request.user
            form.save()
            return redirect("myPosts")
    else:
        form = AddPostForm(instance=post)

    return render(request, "Blog/updatePost.html", {"form": form, "post": post})


@login_required
def deletePost(request, id):
    post = Posts.objects.get(id=id)

    if request.method == "POST":
        post.delete()
        return redirect("myPosts")

    return render(request, "Blog/deletePost.html", {"post": post})
