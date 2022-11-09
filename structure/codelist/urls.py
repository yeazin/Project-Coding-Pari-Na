## Code list app URL paths 

from django.urls import path
from structure.codelist.views import (
     ListInputView,
     ListInputSingleView,
     ListInputDeleteView,
     ListInputViewbyProfile
)


urlpatterns = [
    path('',ListInputView.as_view(),name="list"),
    path('<uuid:valueID>/',ListInputSingleView.as_view(),name='single_list') ,   
    path('delete/<uuid:valueID>/',ListInputDeleteView.as_view(),name='delete_list')

]

api_URL = [
    path('api/v1/list/',ListInputViewbyProfile.as_view())
]

urlpatterns += api_URL