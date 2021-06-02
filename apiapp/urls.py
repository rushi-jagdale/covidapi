from django.urls import path
from . import views


urlpatterns = [
    # path('', views.eventList, name = "events"), 
    # path('create',views.eventCreate, name = "create"),
    path('hlist',views.hospitallist, name="hlist"),
    path('hcreate',views.hospitalCreate, name="hcreate"),
    path('delete/<str:pk>/',views.delete, name="delete"),
    path('update/<str:pk>/',views.update, name="update")

]