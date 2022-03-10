from distutils.log import error
from enum import unique
from rest_framework import serializers

from django.contrib.auth.models import User

validation_errors = {
    'email':{
        'exist' : {
            'email' : 'Email alreay exist',
        }
    }
}

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 30, min_length = 4, write_only = True)
    email = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'id']
        read_only_fields = ('id',)

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email = email):
            raise serializers.ValidationError(validation_errors['email']['exist'])
        return super().validate(attrs)
    
    
    