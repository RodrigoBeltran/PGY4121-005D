
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Usuario
import json
# Create your views here.
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos = {'message': "Usuario encontrado correctamente", 'usuario': usuario}
            else:
                datos = {'message': "Usuario NO encontrado correctamente"}
            return JsonResponse(datos)    
        else:    
            usuarios= list(Usuario.objects.values())
            if len(usuarios)> 0:
                datos = {'message': "Usuarios encontrados correctamente", 'usuarios': usuarios}
            else:
                datos = {'message': "Usuarios no encontrados..."}
            return JsonResponse(datos)

    def post(self,request): 
        jd= json.loads(request.body)
        Usuario.objects.create(nombreUsuario = jd['nombreUsuario'],correo =jd['correo'],contrasena=jd['contrasena'])
        datos ={'message': "Usuario Agregado"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd= json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            usuario = Usuario.objects.get(id=id)
            usuario.nombreUsuario=jd['nombreUsuario']
            usuario.correo=jd['correo']
            usuario.contrasena=jd['contrasena']
            usuario.save()
            datos = {'message': "Usuario modificado correctamente"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)    

    def delete(self,request,id):
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Usuario Borrado correctamente"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)       