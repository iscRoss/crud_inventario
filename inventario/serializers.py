from rest_framework import serializers

from .models import catg_tipo_producto

class serializer_tipo_producto(serializers.ModelSerializer):
    class Meta:
        model = catg_tipo_producto
        fields=("pk_tipo_producto", "tipo_producto")
