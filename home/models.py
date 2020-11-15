from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass


class ShelvesPage(Page):
    pass


class ShelfPage(Page):
    pass


class ShelfModel(models.Model):
    "This model defines the abstract shelf table and the necessary details for each shelf"
    shelf_number = models.IntegerField(unique=True)
    shelf_size = models.CharField(max_length=255)
    shelf_price = models.CharField(max_length=60)
    shelf_description = models.TextField()


class ClientModel(models.Model):
    "This model defines the abstract shelf client table and the necessary details for each Client"

    client_name = models.CharField(max_length=255)
    client_id_number = models.IntegerField()
    client_business_name = models.CharField(max_length=255)
    client_contacts = models.CharField(max_length=255)
    client_status = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)


class CustomerModel(models.Model):
    "This model defines the abstract shelf client table and the necessary details for each Client"
    client_name = models.CharField(max_length=255)
    client_id_number = models.IntegerField()
    client_business_name = models.CharField(max_length=255)
    client_contacts = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)


class ProductModel(models.Model):
    "This model defines the abstract Products client bring to Francan and the necessary details for each Product"
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_item_price = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)


class ClientStockModel(models.Model):
    productmodel = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    client_model = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    product_quantity = models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    no_of_items = models.IntegerField()
