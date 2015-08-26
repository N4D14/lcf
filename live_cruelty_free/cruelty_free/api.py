from tastypie.resources import ModelResource
from tastypie.constants import ALL
from cruelty_free.models import Company


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
