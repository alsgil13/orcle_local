from django import forms
from django.forms import ModelForm
from borrows.models import Item

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy


class SignUpForm(UserCreationForm):
    dt_nasc = forms.DateField(label="Data de Nascimento",help_text='Required. Format: YYYY-MM-DD')
    cep = forms.CharField(max_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','dt_nasc', 'cep', 'password1', 'password2', )

# class ItemForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['nome, autor, descricao, dono, tipo, foto, status']

# class ItemCreate(CreateView):
#     model = Item
#     fields = ['nome, autor, descricao, dono, tipo, foto, status']

# class ItemUpdate(UpdateView):
#     model = Item
#     fields = ['nome, autor, descricao, dono, tipo, foto, status']


# class ItemDelete(DeleteView):
#     model = Item
#     success_url = reverse_lazy('itens')    


