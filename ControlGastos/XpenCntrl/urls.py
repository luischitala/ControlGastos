from django.urls import path
from django.conf.urls import url
from XpenCntrl import views as local_views

app_name = 'XpenCntrl'

urlpatterns = [

    path("", local_views.xpencntrl_index, name="xpencontrl_index"),
    path("category/list/", local_views.CategoryListView.as_view(), name="category_list"),


]