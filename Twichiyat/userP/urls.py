from django.urls import path,re_path
from . import views

app_name = 'userP'
urlpatterns = [
    re_path(r'^signup/$',views.signup_view,name="signup"),
]
 