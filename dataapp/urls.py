from django.urls import path
from .views import DatasetStats, GetData, DescriptiveStatistics, FindNulls


urlpatterns = [
    path("stats/", DatasetStats.as_view(), name = "dataset-stats"), 
    path("dataset/", GetData.as_view(), name = "dataset"),
    path("describe/", DescriptiveStatistics.as_view(), name = "describe"),
    path("findulls/", FindNulls.as_view(), name = "nulls")
]

