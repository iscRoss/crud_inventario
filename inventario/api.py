
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db import transaction
from .models import catg_tipo_producto
from .serializers import serializer_tipo_producto
from django.http import HttpResponse
from rest_framework.utils import json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'inventario/catg_tipoproducto_list.html'

    def get(self, request):
        queryset = catg_tipo_producto.objects.all()
        return Response({'queryset': queryset})
    

class catgInventarioAPI(APIView):

    @transaction.atomic()
    def get(self, request):
        try:
            qs = catg_tipo_producto.objects.values("pk_tipo_producto", "tipo_producto")
            data = list(qs)
        except catg_tipo_producto.DoesNotExist:
            data.append({'error': 'Tipo de producto no existe'})
        return Response(data)
    @transaction.atomic()
    def post(self, request):
        inv_serializer = serializer_tipo_producto(data=request.data)
        if inv_serializer.is_valid():
            inv_serializer.save()
            return JsonResponse(inv_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(inv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class catgInventarioAPI2(APIView):
    serializer = serializer_tipo_producto
    def get(self, request, format=None):
        lista = catg_tipo_producto.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')


class Post_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return catg_tipo_producto.objects.get(pk=pk)
        except catg_tipo_producto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = serializer_tipo_producto(post)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = serializer_tipo_producto(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)