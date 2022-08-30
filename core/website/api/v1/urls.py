from django.urls import path,include
from . import views



urlpatterns = [
    # Registration management
    path("demo/", views.DemoApiView.as_view(), name="demo"),
]
