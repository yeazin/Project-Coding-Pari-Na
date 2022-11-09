'''
This file is created for
    - API endpoint 
'''

from rest_framework import serializers


## importing models 
from structure.accounts.models.profile import Profile
from structure.codelist.models import ListInput


class ListInputserializer(serializers.ModelSerializer):

    class Meta:
        model = ListInput
        fields = ['input_values', 'created_at']


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='id')
    profile_input = ListInputserializer(many=True)
    class Meta:
        model = Profile
        fields = ['user_id','full_name','profile_input']