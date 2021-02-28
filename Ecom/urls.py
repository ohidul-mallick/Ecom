from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from store import views


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name='homepage'),
    path('signup/', views.signUp,name='signup'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.userLogout,name='logout'),
    path('logoutView/', views.userlogoutView,name='logoutView'),
    path('checkout/', views.checkoutView.as_view(),name='checkout'),


    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('item_remove/<int:id>/',
         views.item_remove, name='item_remove'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
