from django.contrib import admin
from django.urls import path,re_path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import settings
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home_page,name="home"),
    re_path(r'^userP/',include("userP.urls")),
    re_path(r'^dashboard/',include("vendor_dashboard.urls")),
    re_path(r'^Store/',include("Store.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
