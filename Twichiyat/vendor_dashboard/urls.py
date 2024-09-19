from django.urls import path,re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
app_name='vendor_dashboard'
urlpatterns = [
    re_path(r'^$',views.dashboard_home,name="dashboard"),
    re_path(r'^updateAccount/$',views.update_account,name="updateAccount"),
    re_path(r'^delete/$',views.delete_account,name="deleteAccount"),
    re_path(r'^product_area/$',views.product_area,name="product_area"),
    re_path(r'^add_product/$',views.add_product,name="add_product"),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    re_path(r'^delete_product/$',views.delete_product, name="delete_product"),
    re_path(r'^search_product/$',views.search_product, name="search_product"),
    path('annuler_commande/', views.annuler_commande , name='annuler_commande'),
    path('approve_commande/', views.approve_command , name='approve_commande'),
    
]
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
