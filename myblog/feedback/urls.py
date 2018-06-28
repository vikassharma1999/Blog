from django.urls import path,re_path
app_name='feedback'
from.import views
urlpatterns=[
path('',views.feed,name='feed'),
path('thanks/',views.thanks,name='thanks'),
path('about/',views.about,name='about'),
]
