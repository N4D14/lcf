from django.conf.urls import url, include
from tastypie.api import Api

from cruelty_free.api import CompanyResource
from cruelty_free import views

cf_api = Api(api_name='cf')
cf_api.register(CompanyResource())

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(cf_api.urls)),
]
