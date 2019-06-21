from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from knox.views import LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/auth/", include("project.users.urls")),
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html"), name="app"),
]
