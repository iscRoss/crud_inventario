from django.db import models

# Create your models here.
class catg_tipo_producto (models.Model):
    pk_tipo_producto = models.AutoField(primary_key = True)
    tipo_producto = models.CharField(max_length = 35)

    class Meta:
        db_table = 'catg_tipo_producto'
    def __str__(self):
        return self.tipo_producto

class inventario (models.Model):
    pk_inventario = models.AutoField(primary_key = True)
    fk_tipo_producto = models.ForeignKey(catg_tipo_producto, null= False, blank = True, on_delete= models.CASCADE)
    nombre_producto = models.CharField(max_length = 35, null= False)
    cantidad_producto = models.PositiveIntegerField(null= False)
    class Meta:
        db_table = 'inventario'
    def __str__(self):
        return self.tipo_producto