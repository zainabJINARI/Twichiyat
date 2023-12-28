from django.urls import path,re_path
from . import views

app_name = 'Store'

urlpatterns = [
	re_path(r'^home/',views.shop_now,name="shopnow"),
    re_path(r'carte/',views.carte, name="cartecredit")
]

