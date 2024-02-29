from django.shortcuts import render
import numpy as np
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from .calculations import about_data, classify_data, descriptive_statistics, nulls
from .Serilizers import DataStatsSerilizers


class DatasetStats(APIView):
    def post(self, request, *args, **kwargs):
        serilizers = DataStatsSerilizers(data = request.data)
        if not serilizers.is_valid():
            return Response(serilizers.errors, status = status.HTTP_400_BAD_REQUEST)
        dataset = serilizers.validated_data.get("dataset")
        response = about_data(dataset)
        return Response(response)
    

class GetData(APIView):
    def post(self, request, format = None):
        serilizers = DataStatsSerilizers(data = request.data)
        if not serilizers.is_valid():
            return Response(serilizers.errors, status = status.HTTP_400_BAD_REQUEST)
        dataset = serilizers.validated_data.get("dataset")
        numeric_data, cat_data, date_time = classify_data(dataset)
        response = {
            "numeric_data":numeric_data,
            "cat_data":cat_data,
            "datetime":date_time
        }
        return Response(response)


class DescriptiveStatistics(APIView):
    def post(self, request, format = None):
        serilizers = DataStatsSerilizers(data = request.data)
        if not serilizers.is_valid():
            return Response(serilizers.errors, status = status.HTTP_400_BAD_REQUEST)
        dataset = serilizers.validated_data.get("dataset")
        statistics = descriptive_statistics(dataset)
        return Response(statistics)
    

class FindNulls(APIView):
    def post(self, request, format = None):
        serilizers = DataStatsSerilizers(data = request.data)
        if not serilizers.is_valid():
            return Response(serilizers.errors, status = status.HTTP_400_BAD_REQUEST)
        dataset = serilizers.validated_data.get("dataset")
        null = nulls(dataset)
        return Response(null)
    
