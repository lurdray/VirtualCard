from django.urls import path
from . import views

app_name = "order"

urlpatterns = [

    path("", views.ShopCartView, name="shopcart"),
    path("shipping/", views.ShippingView, name="shipping"),
    path("complete/", views.CompleteView, name="complete"),
    path("update-profile/", views.UpdateAppuserView, name="update_appuser"),

    path("dashboard/", views.DashboardView, name="dashboard"),
    path("url-profile/", views.URLProfileView, name="url_profile"),

]