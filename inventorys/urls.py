from django.urls import path

urlpatterns = [
        path('', InventorysView.as_view())
]
