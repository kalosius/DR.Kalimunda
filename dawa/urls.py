from django.urls import path
from dawa import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('index/', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout' ),
    # this route is for buying [BUY ITEM]
    path('index/<int:product_id>', views.product_detail, name = 'product_detail')
]
