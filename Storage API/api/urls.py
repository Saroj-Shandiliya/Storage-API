from django.urls import path, include
from .views import itemList, itemDetail, locationList,locationDetail

#we will have 4 api endpoints
# 1 each for all item and location 
# 1 each to view individual data
urlpatterns = [
    path('item/',itemList.as_view()),
    path('item/<int:pk>/',itemDetail.as_view()),
    path('location/',locationList.as_view()),
    path('location/<int:pk>/',locationDetail.as_view()),
]