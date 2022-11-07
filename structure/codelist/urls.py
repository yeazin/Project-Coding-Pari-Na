## Code list app URL paths 

from django.urls import path
from structure.codelist.views import ListInputView


urlpatterns = [
    path('',ListInputView.as_view(),name="list")
]