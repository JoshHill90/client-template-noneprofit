from django.shortcuts import render, redirect
import calendar
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Event
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .serializers import EventSerializer
from logs.logging_config import logging
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Request to get calendar data
@api_view(['GET'])
def get_event_list(request):
    if request.method == "GET":
        try:
            events = Event.objects.all()
            serialized_data = EventSerializer(events, many=True)

            return Response(serialized_data.data)
            # if the logic fails 
        except Exception as e:
            error_logged = f"Error in getting events {e} ---> request infor {request}"
            logging.error(error_logged)
            return HttpResponse({'returned': error_logged})
        
    # not a post request
    else:
        resp = {'returned':'wrong request method'}
        logging.error("Error - wrong request method")
        return Response(resp)  