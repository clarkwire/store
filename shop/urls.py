from django.urls import path
# . = from the 'shop' app ⬇
from . import views

# 📣 Declare the name of the app
app_name = 'shop'

# 🗺 Map urls
urlpatterns = [
    path('', views.allProductCat, name='allProdCat'),
    # 1st 1 maps all products w/o category|2nd 1 maps all products by category
    path('<slug:c_slug>', views.allProductCat, name='products_by_category'),
]
