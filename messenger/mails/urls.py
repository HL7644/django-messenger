from django.urls import path
from .views import mail_create_view, mail_detail_view, mail_list_view

app_name='mails'
urlpatterns=[
    path('', mail_list_view, name="mail_list"),
    path('create/', mail_create_view, name="mail_create"),
    path('detail/<int:id>/', mail_detail_view, name="mail_detail"),
]