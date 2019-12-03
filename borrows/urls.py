from django.urls import path
from borrows import views


urlpatterns = [
    path('', views.index, name='index'),
    path('itens/', views.ItemListView.as_view(), name='itens'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('pessoas/', views.PessoaListView.as_view(), name='pessoas'),
    path('pessoa/<int:pk>', views.PessoaDetailView.as_view(), name='pessoa-detail'),    
    path('sobre', views.sobre, name='sobre'),
    path('meuperfil', views.perfil, name='meu-perfil'),
    #path('accounts/profile', views.PerfilDetailView.as_view(), name='profile'),    

    path('item/create/', views.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),

    path('tipoitem/create/', views.TipoItemCreate.as_view(), name='tipoitem_create'),
    path('tipoitem/<int:pk>/update/', views.TipoItemUpdate.as_view(), name='tipoitem_update'),
    path('tipoitem/<int:pk>/delete/', views.TipoItemDelete.as_view(), name='tipoitem_delete'),

    path('signup', views.signup, name='signup'),
    path('perfil/<int:pk>/update/', views.PerfilUpdate.as_view(), name='perfil_update'),
    path('perfil/<int:pk>/delete/', views.PerfilDelete.as_view(), name='perfil_delete'),


    path('tipoitem/', views.TipoItemListView.as_view(), name='tipoitem'),
    path('meusitens/', views.MeusItensListView.as_view(), name='tipoitem'),
    path('meusemprestimos/', views.MeusEmprestimosListView.as_view(), name='meusemprestimos'),


    path('emprestimo/create/', views.EmprestimoCreate.as_view(), name='emprestimo_create'),
    path('emprestimo/<int:pk>/update/', views.EmprestimoUpdate.as_view(), name='emprestimo_update'),
    path('emprestimo/<int:pk>/delete/', views.EmprestimoDelete.as_view(), name='emprestimo_delete'),

    path('download/', views.download, name='download'),
    path('download_all/', views.downloadALL, name='download_all'),

    path('ari_mazer/', views.ari_mazer, name='ari_mazer'),

]