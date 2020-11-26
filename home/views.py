from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.http import JsonResponse
from wagtail.core.models import Page
from wagtail.search.models import Query
from .models import Shelf, Product, ProductSale, RentPayment, Client
from .forms import ProductForm, StockOutForm, ShelfForm, ClientForm, RentForm
import json


def shelf(request, id):
    data = {
        'shelf': Shelf.objects.get(pk=id),
        'name': "Shelf Number:" + str(id),
        'formid': ''
    }
    print(Shelf.objects.get(pk=id))
    return TemplateResponse(request, 'home/shelf_page.html', data)


def addproduct(request, id):
    form = ProductForm
    data = {
        'form': ProductForm,
        'name': "addProduct"
    }
    print(Shelf.objects.filter(client_owner__isnull=True))
    if request.method == 'GET':
        return TemplateResponse(request, 'home/add_product_page.html', data)


def newproduct(request):
    if request.method == 'POST':
        response_message = None
        error = None
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(Shelf.objects.get(pk=data['product_shelf']))
            new_product = Product(
                product_name=data['product_name'], product_description=data[
                    'product_description'], product_unit_price=data['product_unit_price'],
                no_of_products=data['no_of_products'], product_type=data['product_type'],
                product_brand=data['product_brand'], product_shelf=Shelf.objects.get(pk=data['product_shelf']))

            print(new_product)
            new_product.save()
            response_message = "Successfully saved."
        except Exception as e:
            print(e)
            error = {'message':
                     'An error occured Kindly try again or contact administrator  ' + str(e)}
        # print(data)
        return JsonResponse({
            'message': response_message,
            'error': error
        })


def sellitem(request, id):
    form = StockOutForm
    data = {
        'form': form,
        'name': "Stock Out Product",
        'formid': "sellProduct"
    }
    if request.method == 'GET':
        return TemplateResponse(request, 'home/sell_product.html',  data)


def handle_product_sale(request):
    if request.method == 'POST':
        response_message = None
        error = None
        try:
            data = json.loads(request.body.decode('utf-8'))
            # print(ProductSale.objects.get(pk=data['customer_id']))
            print("Selling")
            new_product_sale = ProductSale(
                product_id=Product.objects.get(pk=data['product_id']), type_of_payment=data[
                    'type_of_payment'], no_of_items=data['no_of_items'],
                customer_name=data['customer_name'], customer_id=data['customer_id'],
            )

            print('We sold', new_product_sale)
            new_product_sale.save()
            response_message = "Successfully saved."
        except Exception as e:
            print('THis error occured', e)
            error = {'message':
                     'An error occured Kindly try again or contact administrator  ' + str(e)}
        # print(data)
        return JsonResponse({
            'message': response_message,
            'error': error,
        })


def add_shelf(request):
    form = ShelfForm
    data = {
        'form': form,
        'name': "Add new Shelf",
        'formid': "addShelf"
    }
    if request.method == 'GET':
        return TemplateResponse(request, 'home/sell_product.html', data)


def handle_add_shelf(request):
    if request.method == 'POST':
        response_message = None
        error = None
        try:
            data = json.loads(request.body.decode('utf-8'))
            # print(ProductSale.objects.get(pk=data['customer_id']))
            print("Selling")
            client = data['client_owner']
            client_owner = None
            if client:
                client_owner = Client.objects.get(
                    pk=data['client_owner'])
            new_shelf = Shelf(
                shelf_number=data['shelf_number'], shelf_size=data[
                    'shelf_size'], shelf_price=data['shelf_price'],
                shelf_description=data['shelf_description'], client_owner=client_owner
            )

            print('We sold', new_shelf)
            new_shelf.save()
            response_message = "Successfully saved."
        except Exception as e:
            print('THis error occured', e)
            error = {'message':
                     'An error occured Kindly try again or contact administrator  ' + str(e)}
        # print(data)
        return JsonResponse({
            'message': response_message,
            'error': error,
        })


def add_client(request):
    form = ClientForm
    data = {
        'form': form,
        'name': "Add new Client",
        'formid': 'addClient'
    }
    if request.method == 'GET':
        return TemplateResponse(request, 'home/sell_product.html', data)


def handle_add_client(request):
    if request.method == 'POST':
        response_message = None
        error = None
        try:
            data = json.loads(request.body.decode('utf-8'))
            # print(ProductSale.objects.get(pk=data['customer_id']))
            print("Selling")
            new_client = Client(
                client_name=data['client_name'],
                client_id_number=data['client_id_number'],
                client_business_name=data['client_business_name'],
                business_type=data['business_type'],
                client_contacts=data['client_contacts'],
                client_email=data['client_email'],
            )

            print('We sold', new_client)
            new_client.save()
            response_message = "Successfully saved."
        except Exception as e:
            print('THis error occured', e)
            error = {'message':
                     'An error occured Kindly try again or contact administrator  ' + str(e)}
        # print(data)
        return JsonResponse({
            'message': response_message,
            'error': error,
        })


def add_rent(request):
    form = RentForm
    data = {
        'form': form,
        'name': 'Rent',
        'formid': 'addRent'
    }
    if request.method == 'GET':
        return TemplateResponse(request, 'home/sell_product.html', data)


def handle_add_rent(request):
    if request.method == 'POST':
        response_message = None
        error = None
        try:
            data = json.loads(request.body.decode('utf-8'))
            # print(ProductSale.objects.get(pk=data['customer_id']))
            print("Rent Payment")
            new_client = RentPayment(
                shelf_id=Shelf.objects.get(pk=data['shelf_id']),
                amount_paid=data['amount_paid'],
                client_name=data['client_name'],
            )

            print('We sold', new_client)
            new_client.save()
            response_message = "Successfully saved."
        except Exception as e:
            print('THis error occured', e)
            error = {'message':
                     'An error occured Kindly try again or contact administrator  ' + str(e)}
        # print(data)
        return JsonResponse({
            'message': response_message,
            'error': error,
        })


def rent_payments(request):
    data = {
        'info': RentPayment.objects.all(),
        'name': 'Rent Payments'
    }
    print(RentPayment.objects.all())
    return TemplateResponse(request, 'home/rent_payments.html', data)
