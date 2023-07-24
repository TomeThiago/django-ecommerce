from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto


def list_products(request):
    if request.method == "GET":
        products = Produto.objects.all()

        return render(request, "list_product.html", {"list_products": products})
    if request.method == "DELETE":
        HttpResponse.status_code(204)

        return HttpResponse.json({"mensagem": "excluido com sucesso"})


def create_product(request):
    if request.method == "GET":
        return render(request, "create_product.html")
    elif request.method == "POST":
        nome = request.POST.get("nome")
        valor = request.POST.get("valor")

        produto = Produto(nome=nome, valor=valor)

        produto.save()

        return render(request, "result_product.html")
