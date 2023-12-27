from django.urls import path,re_path
from . import views

app_name='vendor_dashboard'
urlpatterns = [
    re_path(r'^$',views.dashboard_home,name="dashboard")
]
