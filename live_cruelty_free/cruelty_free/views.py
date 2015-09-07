from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from cruelty_free.forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'search/index.html')


# Login form view
class LoginFormView(TemplateView) :
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        context.update(login_form=LoginForm())
        print('Here in login View!!!')
        return context

    # TODO: fix this
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LoginFormView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('Expected an XMLHttpRequest')

        form_data = json.loads(request.body)
        login_form = LoginForm(data={'username': in_data.get('username'), 
                                     'password': in_data.get('password')})

        # now validate the login form 
        if login_form.is_valid():
            return HttpResponseRedirect('/')       