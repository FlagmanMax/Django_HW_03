from django.urls import path

from .views import index, view_all_clients, view_all_orders_by_client,\
view_all_items_ordered_by_client

urlpatterns = [
    path("", index, name='index'),
    path("view_all_clients/", view_all_clients, name='view_all_clients'),
    path("view_all_orders_by_client/<int:client_id>/", view_all_orders_by_client, name='view_all_orders_by_client'),
    # path("about/", about, name='about'),
    path("view_all_items_ordered_by_client/<int:client_id>/", view_all_items_ordered_by_client, name='view_all_items_ordered_by_client'),
    path("view_all_items_ordered_by_client/<int:client_id>/<int:days>/", view_all_items_ordered_by_client, name='view_all_items_ordered_by_client'),

    ]