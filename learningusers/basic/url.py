from django.conf.urls import url
from basic import views

app_name = 'basic_app'

urlpatterns=[
    url(r'^registration/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
]
