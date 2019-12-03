from django.contrib import admin
from borrows.models import TipoItem, Profile, Item, Emprestimo

# Register your models here.
admin.site.register(TipoItem)
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Emprestimo)
