from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['name', 'brand', 'model', 'category', 'description', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.Select(attrs={'class':'form-control'}),
            'model': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class':'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'brand': 'Marca',
            'model': 'Modelo',
            'category': 'Categoria',
            'description': 'Descrição',
            'serie_number': 'Númro de série',
            'cost_price': 'Preço de compra',
            'selling_price': 'Preço de venda',
            'quantity': 'Quatidade',
            'photo': 'Foto/Imagem',
        }

    def clean(self):
        cleaned_data = super().clean()
        brand = cleaned_data.get('brand')
        model = cleaned_data.get('model')
        category = cleaned_data.get('category')

        # Verificar se já existe outro produto com os mesmos atributos
        existing_product = models.Product.objects.filter(
            brand=brand,
            model=model,
            category=category
        ).exclude(pk=self.instance.pk)  # Ignorar o produto atual

        if existing_product.exists():
            raise forms.ValidationError(
                'Um produto com a mesma marca, modelo e categoria já existe.'
            )

        return cleaned_data