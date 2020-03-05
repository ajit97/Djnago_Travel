from django.urls import path
from . import views

urlpatterns = [
  path("articles/<slug:slug>/", views.article_detail,),
  path('cart/',views.cart)
]