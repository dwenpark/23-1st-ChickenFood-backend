from django.urls import path

from inventorys.views import InventorysView

urlpatterns = [
        path('', InventorysView.as_view())
]
