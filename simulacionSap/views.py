from .serializers import EstadoSerializer, TipoEquipoSerializer, EquipoSerializer, ReparacionSerializer
from .models import Equipo, Estado, Reparacion, TipoEquipo
from rest_framework.decorators import api_view
from rest_framework.response import Response

#vista que devuelva los nombres de los equipos con sus estados
@api_view(['GET'])
def equipos_estado(request):
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return Response(serializer.data)


#vista que devuelva toda la informacion de la reparacion pero en vez del id equipo sea el nombre del equipo
@api_view(['GET'])
def reparaciones_nombre_equipo(request):
    reparaciones = Reparacion.objects.all()
    serializer = ReparacionSerializer(reparaciones, many=True)
    return Response(serializer.data)

