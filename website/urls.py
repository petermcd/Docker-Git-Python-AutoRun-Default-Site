from django.urls import include, path

from website.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]