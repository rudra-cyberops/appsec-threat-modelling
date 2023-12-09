from django.urls import path
from .views import index, logout_view, view_address, create_address

urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout_view, name="logout"),
    path("address/<int:address_id>/", view_address, name="view_address"),
    path("create-address/", create_address, name="create_address"),
]
