from . import views
from django.urls import path

urlpatterns = [    
    path('produto_list', views.produtoList, name='produto_list'),
    path('produto_create', views.produtoCreate, name='produto_create'),
    path('produto_update/<int:id>', views.produtoUpdate, name='produto_update'),
    path('produto_delete/<int:id>', views.produtoDelete, name='produto_delete'),
    path('', views.produtoList, name='produto_list'),
]