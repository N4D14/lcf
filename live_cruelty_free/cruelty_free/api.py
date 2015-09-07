from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from django.contrib.auth.models import User
from cruelty_free.models import Company


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']


class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'
        allowed_methods = ['post', 'get', 'put', 'delete']
        # authentication = Authentication()
        # authorization = Authorization()
        always_return_data = True
        filtering = {
            'name': ALL,
        }
