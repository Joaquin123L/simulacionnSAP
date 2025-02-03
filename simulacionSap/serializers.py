from rest_framework import serializers
from .models import Equipo, Estado, Reparacion, TipoEquipo

# Serializador para el tipo de equipo
class TipoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipo
        fields = ['descripcion']  # Devuelve solo el nombre del tipo de equipo

# Serializador para el estado
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['tipo_estado']  # Devuelve solo el nombre del estado

# Serializador para el equipo
class EquipoSerializer(serializers.ModelSerializer):
    # Agregar el serializador de TipoEquipo y Estado
    id_tipo_equipo = TipoEquipoSerializer()  # Anidar el serializador de TipoEquipo
    id_estado = EstadoSerializer()  # Anidar el serializador de Estado

    class Meta:
        model = Equipo
        fields = ['id_equipo', 'nombre', 'id_tipo_equipo', 'id_estado']  # Incluir solo los campos necesarios

# Serializador para la reparación
class ReparacionSerializer(serializers.ModelSerializer):
    # Incluir el equipo con su nombre
    id_equipo = EquipoSerializer()  # Anidar el serializador de Equipo

    class Meta:
        model = Reparacion
        fields = ['id_reparacion', 'id_equipo', 'motivo', 'fecha_inicio', 'fecha_fin']