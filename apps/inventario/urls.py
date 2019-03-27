from django.contrib import admin
from django.urls import path 
from django.conf.urls import url , include
from . import views


from apps.inventario.views import UsuarioCreate, UsuarioList,usuarioDelete,EquipamientoCreate, AsignacionCreate, pdaCreate, telefonoCreate, UsuarioUpdate,usuarioShow,equipoList,equipoUpdate,equipoDelete,equipoShow,asignacionList,asignacionUpdate,asignacionDelete,asignacionShow,pdaList,pdaUpdate,pdaDelete,pdaShow,telegonoList,telefonoUpdate,telefonoDelete,telefonoShow

app_name = 'inventario'

urlpatterns = [
    #URL paginas principales y login

    
    url(r'^$', views.singIn),
    url(r'^postsign/', views.postsign),
    url(r'^logout/',views.logout,name='log'),
   
    #URLS para mostrar usuarios
    url(r'^nuevoUsuario/', UsuarioCreate.as_view(), name='usuario_crear'),
    url(r'^listarUsuario/', UsuarioList.as_view(), name='usuario_listar'),
    url(r'^EliminarUsuario/(?P<pk>\d+)/$', usuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^EditarUsuario/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^mostrarUsuario/(?P<pk>\d+)/$', usuarioShow.as_view(), name='usuario_mostrar'),
    # URLS para equipamiento
    url(r'^nuevoEquipo/', EquipamientoCreate.as_view(),name='equipo_crear'),
    url(r'^listarequipo/',equipoList.as_view(),name='equipo_listar'),
    url(r'^editarEquipo/(?P<pk>\d+)/$',equipoUpdate.as_view(),name='equipo_editar'),
    url(r'^eliminarEquipo/(?P<pk>\d+)/$',equipoDelete.as_view(),name='equipo_eliminar'),
    url(r'^mostrarEquipo/(?P<pk>\d+)/$',equipoShow.as_view(),name='equipo_mostrar'),
  
    #URLS para asignacion
    url(r'^nuevaAsignacion/', AsignacionCreate.as_view(),name='asignacion_crear'),
    url(r'^listarAsignacion/',asignacionList.as_view(),name='asignacion_listar'),
    url(r'^editarAsignacion/(?P<pk>\d+)/$',asignacionUpdate.as_view(),name='asignacion_editar'),
    url(r'^eliminarAsignacion/(?P<pk>\d+)/$',asignacionDelete.as_view(),name='asignacion_eliminar'),
    url(r'^mostrarAsignacion/(?P<pk>\d+)/$',asignacionShow.as_view(),name='asignacion_mostrar'),
    #URLS para pda
    url(r'^nuevaPda/', pdaCreate.as_view(),name='pda_crear'),
    url(r'^listarpda/',pdaList.as_view(),name='pda_listar'),
    url(r'^editarPda/(?P<pk>\d+)/$',pdaUpdate.as_view(),name='pda_editar'),
    url(r'^eliminarPda/(?P<pk>\d+)/$',pdaDelete.as_view(),name='pda_eliminar'),
    url(r'^mostrarPda/(?P<pk>\d+)/$',pdaShow.as_view(),name='pda_mostrar'),
    #URL para telefono
    url(r'^nuevoTelefono/', telefonoCreate.as_view(),name='telefono_crear'),
    url(r'^listarTelefono/',telegonoList.as_view(),name='telefono_listar'),
    url(r'^editarTelefono/(?P<pk>\d+)/$',telefonoUpdate.as_view(),name='telefono_editar'),
    url(r'^eliminarTelefono/(?P<pk>\d+)/$',telefonoDelete.as_view(),name='telefono_eliminar'),
    url(r'^mostrarTelefono/(?P<pk>\d+)/$',telefonoShow.as_view(),name='telefono_mostrar')
]