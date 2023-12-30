from django.contrib import admin
from django.urls import path
from Blog import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("update/", views.updateprofile, name="updateprofile"),
    path("password/", views.updatepassword, name="password"),
    path(
        "",
        LoginView.as_view(
            template_name="Blog/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("signup/", views.signuppage, name="signup"),
    path("logout/", views.logoutpage, name="logout"),
    path("myPosts/", views.myPosts, name="myPosts"),
    path("addPost/", views.addPost, name="addPost"),
    path("post-<int:id>/update/", views.updatePost, name="updatePost"),
    path("post-<int:id>/delete/", views.deletePost, name="deletePost"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
