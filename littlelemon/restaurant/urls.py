# define URL route for index() view
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
]


booking_router = DefaultRouter()
booking_router.register("tables", views.BookingViewSet)
