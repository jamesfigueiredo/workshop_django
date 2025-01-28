from django import forms
from django.core.exceptions import ValidationError
from . import models


class SaleForm(forms.ModelForm):

    class Meta:
        model = models.Sale
        fields = ['product', 'quantity', 'descrition']
        widgets = {
            'product': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'descrition': forms.Textarea(attrs={'class':'form-control', 'rows': 3}),

        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'descrition': 'Descrição',
        }

    # Validação do formulário de saída/vendas
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade em estoque do produto {product.name} é de: {product.quantity}'
            )
        return quantity