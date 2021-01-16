from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core.models import Contato


def home(request):
    return render(request, 'index.html')

def produtos(request):
    return render(request, 'produtos.html')

def empresa(request):
    return render(request, 'empresa.html')

@login_required
def contato(request):
    if request.method == 'GET':
        contatos = Contato.objects.filter(ativo=True).order_by('-data_criacao')
        context = {
            'contatos': contatos,
        }
        return render(request, 'contato.html', context)
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            comment =  request.POST.get('comment')
            Contato.objects.create(nome=nome, email=email, conteudo=comment)
            return JsonResponse("Gravou", safe=False)
        except Exception as e:
            return JsonResponse("Erro" + e, safe=False)

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
    if request.method == 'POST':
        loginuser = request.POST['login']
        senhauser = request.POST['senha']
        usuario = authenticate(request, username=loginuser, password=senhauser)
        if usuario is not None:
            login(request, usuario)
            return redirect('/contato/')
        else:
            return render(request, 'logar.html', {'erro': 'Não foi possível logar'})


class PagadorShipay:

    def __init__(self, url_api, total_frete=0):
       self.url_api = url_api
       self.total_frete = total_frete

    @staticmethod
    def convert_to_float(number):
            return float(number)

    @classmethod
    def calcular_carrinho(cls, request):
        if request.method == 'GET':
            total_desconto = 11.35
            total_frete = cls.convert_to_float(request.GET.get('frete'))
            total_carrinho = 0.00
            total_value = 0.00

            list_items = [{
                    'product_name': 'Frete',
                    'quantity': 1,
                    'value_item': round(total_frete, 2)
                }]

            for item in range(2):
                list_items.append({
                    'product_name': 'Itens',
                    'quantity': 5,
                    'value_item': round(189.99, 2)
                })
                total_carrinho += round(189.99 * 5, 2)
            desconto_percent = 1 - total_desconto / 100
            if total_desconto > 0:
                calcular_desconto = total_carrinho + total_frete - (total_carrinho + total_frete * desconto_percent)
                calcular_desconto = round(calcular_desconto / len(list_items), 2)
                for item in list_items:
                    desconto_item = round(item['value_item'] - calcular_desconto, 2)
                    item['value_item'] = desconto_item
            
            for item in list_items:
                calcular_total = round(item['value_item'] * item['quantity'], 2)
                total_value += calcular_total
            print(list_items)
            print("{:.2f}".format(total_value))

            return JsonResponse('teste', status=200, safe=False)
        