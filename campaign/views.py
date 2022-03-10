from xml.dom import ValidationErr
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from .serializers import CampaignImageSerializer, CommentSerializer, CampaignSerializer, RecieverLoactionSearializer
from .models import Campaign


class CampaignListCreateView(APIView):
    
    def post(self, request):
        data = request.data
        data['owner'] = 1
        serializer = CampaignSerializer(data = data)

        serializer.is_valid(raise_exception= True)
        serializer.save()

        res_data = {
            'status' : 'success',
            'payload' : serializer.data
        }

        return Response(res_data, status = status.HTTP_201_CREATED)


    def get(self, request):
        campaign = Campaign.objects.all()
        serializer = CampaignSerializer(campaign, many = True)

        res_data = {
            'status' : 'success',
            'payload' : serializer.data
        }

        return Response(res_data, status=status.HTTP_200_OK)


class CampaignPKView(APIView):
    def get(self, request, *args, **kwargs):
        slug = kwargs['pk']
        try:
            data = Campaign.objects.get(slug = slug)
        except:
            data = None
        
        if data:
            serializer = CampaignSerializer(data)
            res_data = {
                'status' : 'success',
                'payload' : serializer.data
            }
        else:
            res_data = {
                'message' : 'not found'
            }

        return Response(res_data, status = status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        query = {}
        if pk.isnumeric():
            query['id'] = pk
        else:
            query['slug'] = pk

        try:
            campaign = Campaign.objects.get(**query)
            campaign.delete()
            res_data = {
                'status' : 'succss',
                "data" : {}
            }

            return Response(res_data, status = status.HTTP_204_NO_CONTENT)

        except:
            res_data = {
                'status' : 'fail',
                'message' : 'no record found'
            }
            return Response(res_data, status = status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        query = {}
        if pk.isnumeric():
            query['id'] = pk
        else:
            query['slug'] = pk
        
        try:
            campaign = Campaign.objects.get(**query)
        except:
            res_data = {
                'status' : 'fail',
                'message' : 'No record found'
            }
            return Response(res_data, status = status.HTTP_400_BAD_REQUEST)
       
            
        serailizer = CampaignSerializer(instance=campaign, data=request.data, partial = True)
        serailizer.is_valid(raise_exception= True)
        serailizer.save()

        res_data = {
            'status' : 'succss',
            "data" : serailizer.data
        }
        return Response(res_data, status = status.HTTP_200_OK)
        
            

       

