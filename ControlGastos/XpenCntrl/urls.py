from django.urls import path
from django.conf.urls import url
from XpenCntrl import views as local_views

app_name = 'XpenCntrl'

urlpatterns = [

    path("app/", local_views.xpencntrl_index, name="xpencontrl_index"),


]