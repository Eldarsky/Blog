from django import  forms

class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=10)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField(max_value=10)
    rating = forms.FloatField(max_value=10)

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=5, label='Отзывы')