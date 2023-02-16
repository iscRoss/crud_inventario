from django.shortcuts import render
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import catg_tipo_producto
from .serializers import serializer_tipo_producto
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request, 'index.html')
def form_catg_tipoproducto(request):
    return render(request, 'inventario/catg_tipoproducto_post.html')

def form_edit_catg_tipoproducto(request, pk):
    return render(request, 'inventario/catg_tipoproducto_put.html',{'pk':pk})



@api_view(['GET', 'POST'])
def tipo_producto_list(request):
    if request.method == 'GET':
        tipo_products = catg_tipo_producto.objects.all()
        tipo_producto = request.query_params.get('tipo_producto', None)
        
        if tipo_producto is not None:
            tipo_products = catg_tipo_producto.filter(tipo_producto__icontains=tipo_producto)
        inv_serializer = serializer_tipo_producto(tipo_products, many=True)
        return JsonResponse(inv_serializer.data, safe=False)

    elif request.method == 'POST':
        inventario_json = JSONParser().parse(request)
        inv_serializer = serializer_tipo_producto(data=inventario_json)
        if inv_serializer.is_valid():
            inv_serializer.save()
            return JsonResponse(inv_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(inv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tipo_producto_detail(request, pk):
    try: 
        tipo_producto = catg_tipo_producto.objects.get(pk=pk) 
    except catg_tipo_producto.DoesNotExist: 
        return JsonResponse({'message': 'Tipo producto no existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        inv_serializer = serializer_tipo_producto(tipo_producto) 
        return JsonResponse(inv_serializer.data) 
 
    elif request.method == 'PUT': 
        inventario_json = JSONParser().parse(request)
        inv_serializer = serializer_tipo_producto(tipo_producto, data=inventario_json) 
        if inv_serializer.is_valid():
            print(inv_serializer)
            inv_serializer.save() 
            return JsonResponse(inv_serializer.data) 
        return JsonResponse(inv_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tipo_producto.delete() 
        return JsonResponse({'message': 'Tipo de producto eliminado'}, status=status.HTTP_204_NO_CONTENT)
    
        