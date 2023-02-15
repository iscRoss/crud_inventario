from django.urls import path 
from .api import *
from .views import *
urlpatterns = [
    path('api-list', (catgInventarioAPI.as_view()), name = 'api-list'),
    path('api-list2', (catgInventarioAPI2.as_view()), name = 'api-list2'),
    path('api-list/<int:pk>', Post_APIView_Detail.as_view()),
    
    path('api-index-list', (ProfileList.as_view()), name = 'api-index-list'),
    path('tipo-producto-form', (form_catg_tipoproducto), name = 'tipo-producto-form'),
    path('api-put/<int:pk>', (form_edit_catg_tipoproducto), name = 'api-put'),

    path('def-list', (tipo_producto_list), name = 'def-list'),
    path('def-list/<int:pk>',tipo_producto_detail, name = 'editar-tipoproducto'), 

]