from django.urls import path

from .views import (
    PersonListView,
    BulkImportView
)

urlpatterns = [
    path(
        "persons/",
        PersonListView.as_view()
    ),

    path(
        "persons/bulk-import/",
        BulkImportView.as_view()
    ),
]