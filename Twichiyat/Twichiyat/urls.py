from django.contrib import admin
from django.urls import path,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import settings
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home_page,name="home")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
