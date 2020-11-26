from django.db import models
from django.contrib import admin
from wagtail.core.models import Page


class HomePage(Page):

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['info'] = Shelf.objects.all()
        return context


class ShelvesPage(Page):
    def get_context(self, request):
        context = super(ShelvesPage, self).get_context(request)
        context['info'] = Shelf.objects.all()
        return context


class ShelfPage(Page):
    pass


class ClientsPage(Page):
    def get_context(self, request):
        context = super(ClientsPage, self).get_context(request)
        context['info'] = Client.objects.all()
        return context


class CustomersPage(Page):
    pass


class SalesPage(Page):
    pass


class RentsPage(Page):
    pass


class ProductsPage(Page):
    def get_context(self, request):
        context = super(ProductsPage, self).get_context(request)
        context['products'] = Product.objects.all()
        return context


class Client(models.Model):
    "This model defines the abstract shelf client table and the necessary details for each Client"

    def __str__(self):
        return self.client_name
    client_name = models.CharField(max_length=255)
    client_id_number = models.IntegerField()
    client_business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=200)
    photo = models.ImageField(
        upload_to='images', default="avatar.png")
    date = models.DateTimeField(auto_now_add=True)
    client_contacts = models.CharField(max_length=255)
    client_status = models.BooleanField(default=True)
    client_email = models.CharField(max_length=255)


class Shelf(models.Model):
    "This model defines the abstract shelf table and the necessary details for each shelf"

    def __str__(self):
        return ('shelf number: '+str(self.shelf_number))
    shelf_number = models.CharField(unique=True, max_length=255)
    shelf_size = models.CharField(max_length=255)
    shelf_price = models.CharField(max_length=60)
    shelf_description = models.TextField()
    client_owner = models.ForeignKey(
        Client, on_delete=models.DO_NOTHING, blank=True, null=True)


class Product(models.Model):
    "This model defines the abstract Products client bring to Francan and the necessary details for each Product"

    def __str__(self):
        return self.product_name
    product_name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='images', default='images/product1.jpg')
    product_description = models.TextField()
    product_unit_price = models.CharField(max_length=255)
    no_of_products = models.IntegerField()
    product_type = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=255)
    product_shelf = models.ForeignKey(
        Shelf, on_delete=models.CASCADE)


Payment_choices = [
    ("Paid to owner", 'Paid to owner'),
    ("Cash payment", 'Cash Payment'),
]


class ProductSale(models.Model):

    def __str__(self):
        return self.product_id.product_name
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    type_of_payment = models.CharField(max_length=20, choices=Payment_choices)
    no_of_items = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


class RentPayment(models.Model):
    def __str__(self):
        return self.client_name + ' payment'

    shelf_id = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING)
    client_id = models.CharField(max_length=255)
    amount_paid = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=255)


admin.site.register(Shelf)
admin.site.register(Client)
admin.site.register(ProductSale)
admin.site.register(Product)
admin.site.register(RentPayment)
