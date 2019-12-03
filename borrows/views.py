from django.shortcuts import render, redirect
from borrows.models import TipoItem, Item, Profile, Emprestimo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from orcle_django import settings
from borrows.forms import SignUpForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import login, authenticate
from django import forms
import requests



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.dt_nasc = form.cleaned_data.get('dt_nasc')
            user.profile.cep = form.cleaned_data.get('cep')
            viacep = 'http://viacep.com.br/ws/' + str(user.profile.cep) + '/json'
            r = requests.get(viacep)
            user.profile.cidade = r.json()['localidade']
            user.profile.estado = r.json()['uf']
            user.profile.pais = 'Brasil'
            #Usar requests para pegar cidade estado e pais
            user.save()
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('sobre')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def index(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

@login_required
def sobre(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sobre.html')

# --------------- Perfil ----------------------------------


class PerfilUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['dt_nasc','cep','cidade','estado','pais','foto']
    success_url = reverse_lazy('itens')   


class PerfilDelete(LoginRequiredMixin,DeleteView):
    model = Profile
    success_url = reverse_lazy('itens')    

@login_required
def perfil(request):
    usuario = Profile.objects.get(pk=request.user)
    itens = Item.objects.filter(dono=request.user)
    nome = request.user.first_name + " " + request.user.last_name
    dt_nasc = usuario.dt_nasc
    foto = usuario.foto.url
    cidade = usuario.cidade
    estado = usuario.estado
    idusr = request.user.id

    listaitens = []
    for i in itens:
        dados = {
            'item': i
        }
        listaitens.append(i)

    #Criar Contexto
    context = {
        'nome'   : nome,
        'dt_nasc' : dt_nasc,
        'foto' : foto,
        'itens' : listaitens,
        'cidade' : cidade,
        'estado' : estado,
        'id' : idusr,

    }

    return render(request, 'meuperfil.html', context=context)




class MeusItensListView(LoginRequiredMixin, generic.ListView):
    model = Item   
    paginate_by = 3
    def get_queryset(self):
        return Item.objects.filter(dono=self.request.user)
    template_name = 'borrows/meusitens_list.html'


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item   
    paginate_by = 3 

class TipoItemListView(LoginRequiredMixin, generic.ListView):
    model = TipoItem
    paginate_by = 4  

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item    

class PessoaListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    paginate_by = 3    

class PessoaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile        

# class PerfilDetailView(generic.DetailView):
#     model = Profile         




# class CadastraItem(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['nome, autor, descricao, dono, tipo, foto, status']


# CRUD Genérico do Django
# --------------- Item ----------------------------------
class ItemCreate(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   

    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin,UpdateView):
    model = Item
    fields = ['nome', 'autor', 'descricao', 'tipo', 'foto', 'status']
    success_url = reverse_lazy('itens')   


class ItemDelete(LoginRequiredMixin,DeleteView):
    model = Item
    success_url = reverse_lazy('itens')    

# --------------- TipoItem ----------------------------------

class TipoItemCreate(LoginRequiredMixin,CreateView):
    model = TipoItem
    fields = '__all__'
    success_url = reverse_lazy('itens')   

class TipoItemUpdate(LoginRequiredMixin,UpdateView):
    model = TipoItem
    fields = '__all__'
    success_url = reverse_lazy('itens')   


class TipoItemDelete(LoginRequiredMixin,DeleteView):
    model = TipoItem
    success_url = reverse_lazy('itens')    





# --------------- Empréstimo ----------------------------------


class MeusEmprestimosListView(LoginRequiredMixin, generic.ListView):
    model = Emprestimo   
    paginate_by = 4
    def get_queryset(self):
        usuario = self.request.user
        return Emprestimo.objects.filter(item__dono=usuario)
        #return Emprestimo.objects.all().filter(dono=usuario)
    template_name = 'borrows/meusemprestimos_list.html'


class EmprestimoCreate(LoginRequiredMixin,CreateView):
    model = Emprestimo
    fields = ['dtEmprestimo']
    dtEmprestimo = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    success_url = reverse_lazy('itens')   
    
    def form_valid(self, form):
        form.instance.pessoa = self.request.user
        form.instance.aberto = True
        i = Item.objects.get(pk=self.request.GET['item'])
        form.instance.item = i
        return super().form_valid(form)



class EmprestimoUpdate(LoginRequiredMixin,UpdateView):
    model = Emprestimo
    fields = ['dtDevolucao']
    dtDevolucao = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    success_url = reverse_lazy('itens')
    def form_valid(self, form):
        form.instance.aberto = True
        i = Item.objects.get(pk=form.instance.item.id)
        i.status = 'e'
        i.save()
        return super().form_valid(form)   


class EmprestimoDelete(LoginRequiredMixin,UpdateView):
    model = Emprestimo
    fields = ['dtDevolucao']
    dtDevolucao = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    success_url = reverse_lazy('itens') 
    
    def form_valid(self, form):
        form.instance.aberto = False
        i = Item.objects.get(pk=form.instance.item.id)
        i.status = 'd'
        i.save()
        return super().form_valid(form)   





#Servir arquivo

# import tarfile
# from io import BytesIO


# def serve_file(request):
#     out = BytesIO()
#     tar = tarfile.open(mode = "w:gz", fileobj = out)
#     data = 'lala'.encode('utf-8')
#     file = BytesIO(data)
#     info = tarfile.TarInfo(name="1.txt")
#     info.size = len(data)
#     tar.addfile(tarinfo=info, fileobj=file)
#     tar.close()

#     response = HttpResponse(out.getvalue(), content_type='application/tgz')
#     response['Content-Disposition'] = 'attachment; filename=myfile.tgz'
#     return response





@login_required
def download(request):
    import zipfile
    from django.http import HttpResponse
#Define dados do arquivo
    NOME = 'backup.json'
    itens = Item.objects.filter(dono = request.user)
    itemlist = '{'
    for i in itens:
        itemlist += "'"+str(i.id)+"'" + " : " + "'"+str(i)+"'" + ",\n"
    itemlist = itemlist[0:-3]
    itemlist += '}'
    ZIPFILE_NAME = 'orcle_meusitens.zip'



    response = HttpResponse(content_type='application/zip')
    zf = zipfile.ZipFile(response, 'w')
    zf.writestr(NOME, itemlist)
    response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
    return response


@login_required
def downloadALL(request):
    import zipfile
    from django.http import HttpResponse

    #Itens
    NOME_ITENS = 'itens.json'
    itens = Item.objects.all()
    itemlist = '{'
    for i in itens:
        novoitem = '{'+str(i.id) + ":{\n"
        novoitem += "\tnome :" + "'"+ str(i.nome) + "',\n"
        novoitem += "\tautor :" + "'"+ str(i.autor) + "',\n"
        novoitem += "\tdescricao :" + "'"+ str(i.descricao) + "',\n"
        novoitem += "\tdono :" + "'"+ str(i.dono) + "',\n"
        novoitem += "\ttipo :" + "'"+ str(i.tipo) + "',\n"
        novoitem += "\tfoto :" + "'"+ str(i.foto.url) + "',\n"
        novoitem += "\tstatus :" + "'"+ str(i.status) + "',\n"
        novoitem += "\tdtCadastro :" + str(i.dtCadastro) + "\n\t},\n"
        itemlist += novoitem    
    itemlist = itemlist[0:-2]
    itemlist += '\n}'
    
    #Perfis
    NOME_USUARIOS = 'users.json'
    usuarios = Profile.objects.all()
    usuariolist = '{'
    for u in usuarios:
        novousuario = '{'+str(u.user.id) + ":{\n"
        novousuario += "\tdt_nasc :" + "'"+ str(u.dt_nasc) + "',\n"
        novousuario += "\tcep :" + str(u.cep) + ",\n"
        novousuario += "\tcidade :" + "'"+ str(u.cidade) + "',\n"
        novousuario += "\testado :" + "'"+ str(u.estado) + "',\n"
        novousuario += "\tpais :" + "'"+ str(u.pais) + "',\n"
        novousuario += "\tfoto :" + "'"+ str(u.foto.url) + "\n\t},\n"
        usuariolist += novousuario    
    usuariolist = usuariolist[0:-2]
    usuariolist += '\n}'
    
    #Tipos de Item
    NOME_TIPOS = 'tipos.json'
    tipos = TipoItem.objects.all()
    tipolist = '{'
    for t in tipos:
        novotipo = '{'+str(t.id) + ":{\n"
        novotipo += "\tnome :" + "'"+ str(t.nome) + "',\n"
        novotipo += "\tdescrcao :" + "'"+ str(t.descricao) + "\n\t},\n"
        tipolist += novotipo    
    tipolist = tipolist[0:-2]
    tipolist += '\n}'

    #empréstimos
    NOME_EMPRESTIMOS = 'emprestimos.json'
    emprestimos = Emprestimo.objects.all()
    emprestimolist = '{'
    for e in emprestimos:
        novoemprestimo = str(e.id) + ":{\n"
        novoemprestimo += "\tdtEmprestimo :" + str(e.dtEmprestimo) + ",\n"
        novoemprestimo += "\titem :" + "'"+ str(e.item.id) + "',\n"
        novoemprestimo += "\tpessoa :" + "'"+ str(e.pessoa) + "',\n"
        novoemprestimo += "\tdtDevolucao :" + str(e.dtDevolucao) + ",\n"
        novoemprestimo += "\taberto :" + "'"+ str(e.aberto) + "',\n"
        novoemprestimo += "\tdtCadastro :" + str(e.dtCadastro) + "\n\t},\n"
        emprestimolist += novoemprestimo    
    emprestimolist = emprestimolist[0:-2]
    emprestimolist += '\n}'

    ZIPFILE_NAME = 'orcle_backup.zip'

    response = HttpResponse(content_type='application/zip')
    zf = zipfile.ZipFile(response, 'w')
    zf.writestr(NOME_ITENS, itemlist)
    zf.writestr(NOME_USUARIOS, usuariolist)
    zf.writestr(NOME_TIPOS, tipolist)
    zf.writestr(NOME_EMPRESTIMOS, emprestimolist)

    response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
    return response    

def ari_mazer(request):
    """Página Inicial do site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'ari_mazer.html')    