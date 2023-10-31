from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import  JsonResponse
from django.views import View
from django.shortcuts import HttpResponsePermanentRedirect
from django.urls import reverse


from common.views import TitleMixin
from products.models import Product
from users.models import Token, CustomUser
from products.forms import NewGoodForm




class IndexView(TitleMixin, TemplateView):
    title = 'Store'
    template_name = 'products/index.html'


class ProductListView(TitleMixin, ListView):
    title = 'Store - Продукты'
    template_name = 'products/list.html'
    model = Product
    paginate_by = 10


class GenerateTokenView(TitleMixin, View):
    title = 'Store - Получение токена'
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user

            try:
                user_token = CustomUser.objects.get(username=user)
            except CustomUser.DoesNotExist:
                user_token = CustomUser(username=user)

            token, token_created = Token.objects.get_or_create(user=user_token)
            
            if token_created:   
                message = 'You are authenticated. Your new token: ' + str(token.value)

            else:
                message = ' Your token: ' + str(token.value) if token.value else 'No token associated with the user.'

            user_token.token = token.value
            user_token.save()

            return JsonResponse({'message': message})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
class NewGoodView(TitleMixin, View):
    title = 'Store - Добавление товара'
    def get(self, request):
        user = request.user
        token = user.token if user.is_authenticated else None 
        if token:
            context = {'token': token, 'form': NewGoodForm()}
            return render(request, 'users/add_product.html', context)
        else:
            return JsonResponse({'error': 'Take your token'})           

    def post(self, request):
        user = request.user
        token = user.token if user.is_authenticated else None 
        form = NewGoodForm(request.POST)
        if form.is_valid() and token:
            product = Product(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount'],
            )
            product.save()
            return HttpResponsePermanentRedirect(reverse('products:list'))