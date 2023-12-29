from django.urls import path,re_path
from . import views

app_name = 'Store'

urlpatterns = [
	re_path(r'^home/',views.shop_now,name="shopnow"),
	re_path(r'carte/',views.carte, name="cartecredit"),
    re_path(r'liste/',views.file_product,name="file_product"),
    re_path(r'prodliset/',views.productlist,name="productlist"),
    path('product_category/<int:category_id>/',views.product_category,name='product_category'),
    path('products/<int:product_id>/',views.product_details,name='product_detail')
]

