
from django.urls import path
from django.urls import path, re_path
app_name='articles'
from.import views
urlpatterns = [
    path('',views.article_list ,name='list'),
    path('create',views.article_create,name='create'),
    re_path('^(?P<slug>[\w-]+)/$',views.article_details,name='details'),
]
