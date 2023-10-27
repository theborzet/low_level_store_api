from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required


from common.views import TitleMixin
from products.models import Product
from users.models import Token
from products.forms import NewGoodForm




class IndexView(TitleMixin, TemplateView):
    title = 'Store'
    template_name = 'products/index.html'


class ProductListView(TitleMixin, ListView):
    title = 'Store - Продукты'
    template_name = 'products/list.html'
    model = Product
    paginate_by = 10


class GenerateTokenView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': str(token.value)})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)

class NewGoodView(View):
    @login_required(login_url=None)
    def get(self, request):
        token_value = request.session.get('user_token', None)
        if not token_value:
            return HttpResponse('Token must be present.', status=401)
        try:
            token = Token.objects.get(value=token_value)
            token_value = token.value
        except Token.DoesNotExist:
            return HttpResponse('Token is invalid.', status=401)
        context = {'token': token_value, 'form': NewGoodForm()}
        return render(request, 'add_product.html', context)
    

    def post(self, request):
        token_value = request.session.get('user_token', None)
        if not token_value:
            return HttpResponse('Token must be present.', status=401)
        try:
            token = Token.objects.get(value=token_value)
            token_value = token.value        
        except Token.DoesNotExist:
            return HttpResponse('Token is invalid.', status=401)
        form = NewGoodForm(request.POST)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price']
            )
            product.save()
        else:
            context = {'token': token_value, 'form': form}  
            return render(request, 'add_product.html', context)
