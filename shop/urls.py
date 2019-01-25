from django.urls import path
# . = from the 'shop' app ⬇
from . import views

# 📣 Declare the name of the app
app_name = 'shop'

# 🗺 Map urls
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
]
