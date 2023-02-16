from django.urls import path 
from .api import *
from .views import *
urlpatterns = [

    #URL index con qs GET
    path('api-index-list', (ProfileList.as_view()), name = 'api-index-list'),
    #URL de desplege de formulario de inserción POST
    path('tipo-producto-form', (form_catg_tipoproducto), name = 'tipo-producto-form'),
    #URL de desplege de formulario para edición PUT
    path('api-put/<int:pk>', (form_edit_catg_tipoproducto), name = 'api-put'),

    #Servicios APIVIEW
    #GET-POST
    path('api-list', (catgInventarioAPI.as_view()), name = 'api-list'),
    #GET
    path('api-list2', (catgInventarioAPI2.as_view()), name = 'api-list2'),
    #GET-PUT-DELETE
    path('api-list/<int:pk>', Post_APIView_Detail.as_view()),
    
    #Servicios def
    #GET-POST
    path('def-list', (tipo_producto_list), name = 'def-list'),
    #GET-PUT-DELETE
    path('def-list/<int:pk>',tipo_producto_detail, name = 'editar-tipoproducto'), 

]