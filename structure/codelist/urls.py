## Code list app URL paths 

from django.urls import path
from structure.codelist.views import (
     ListInputView,
     ListInputSingleView
)


urlpatterns = [
    path('',ListInputView.as_view(),name="list"),
    path('<uuid:valueID>/',ListInputSingleView.as_view(),name='single_list')
]