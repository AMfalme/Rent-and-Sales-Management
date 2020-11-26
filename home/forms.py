from django import forms

from .models import Shelf, Product, ProductSale, Client, RentPayment


class ContactMessageForm(forms.ModelForm):
    """
    A form for sending the message. Here we're using a Django ModelForm, but this could
    be as simple or as complex as you like -
    see https://docs.djangoproject.com/en/1.9/topics/forms/
    """
    class Meta:
        model = Shelf
        fields = ['shelf_number', 'shelf_size',
                  'shelf_price', 'shelf_description']


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })
        self.fields['product_shelf'].queryset = Shelf.objects.filter(
            client_owner__isnull=True)

    class Meta:
        model = Product
        fields = ['product_shelf', 'product_name', 'photo',
                  'product_unit_price', 'no_of_products', 'product_type',
                  'product_brand', 'product_description'
                  ]


class StockOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StockOutForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })

    class Meta:
        model = ProductSale
        fields = ['product_id',
                  'type_of_payment',
                  'no_of_items',
                  'customer_name',
                  'customer_id',

                  ]


class ShelfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShelfForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })

    class Meta:
        model = Shelf
        fields = [
            'shelf_number',
            'shelf_size',
            'shelf_price',
            'client_owner',
            'shelf_description',

        ]


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })

    class Meta:
        model = Client
        fields = [

            'client_name',
            'client_email',
            'client_id_number',
            'client_business_name',
            'photo',
            'business_type', 'client_contacts',

        ]


class RentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })

    class Meta:
        model = RentPayment
        fields = [
            'shelf_id',
            'client_id',
            'amount_paid',
            'client_name',
        ]
