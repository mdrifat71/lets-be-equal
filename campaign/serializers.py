

from rest_framework import serializers

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from authentication.serializers import UserSerializer

from .models import Campaign
from .models import Campaign, CampaignImage, Comment,  RecieverLocation


errors = {
    'slug' : {
        'exists' : {
            'slug' : 'slug should be unique'
        }
    }
}

class CampaignImageSerializer(serializers.Serializer):
    class Meta:
        model = CampaignImage
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields  = '__all__'

class RecieverLoactionSearializer(serializers.ModelSerializer):
    class Meta:
        model = RecieverLocation
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    location = RecieverLoactionSearializer(required = False)
    raised_ammount = serializers.DecimalField(max_digits=15, decimal_places=6),
    created_at = serializers.DateTimeField(),
    updated_at = serializers.DateTimeField(),
    owner = UserSerializer(read_only = True)


    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ('raised_ammount', 'created_at', 'updated_at')

    
    
    def validate(self, attrs):
        if attrs.get('slug') is not None:
            attrs['slug'] = slugify(attrs['slug'])
        attrs['owner'] = User.objects.get(id = 2)

        campaign = Campaign.objects.filter(slug = attrs.get('slug', ''))
        if campaign:
            raise serializers.ValidationError(errors['slug']['exists'])
        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data.get('location') is not None:
           validated_data['location'] = RecieverLocation.objects.create(**validated_data['location'])
        
        campaign = Campaign.objects.create(**validated_data)
        return campaign





