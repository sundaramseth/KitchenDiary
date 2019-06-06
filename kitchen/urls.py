from django.urls import path

from . import views

urlpatterns = [
         path('',views.index, name='index'),
         path('method/',views.method, name='method'),
         path('applegrumb/', views.applegrumb, name='applegrumb'),
         path('egg/', views.egg, name='egg'),
         path('meatloaf/', views.meatloaf, name='meatloaf'),
         path('quinaoupma/', views.quinaoupma, name='quinaoupma'),
         path('raw/', views.raw, name='raw'),
         path('keema/', views.keema, name='keema'),
         path('baigan/', views.baigan, name='baigan'),
         path('fish/', views.fish, name='fish'),
         path('aloo/', views.aloo, name='aloo'),
         path('Apolo',views.Apolo, name='Apolo'),
         path('cchiken',views.cchiken, name='cchiken'),
         path('dal',views.dal, name='dal'),
         path('noodle',views.noodle, name='noodle'),
         path('pork',views.pork, name='pork'),
         path('sahi',views.sahi, name='sahi'),
         path('saunpa',views.saunpa, name='saunpa'),
         path('sejwan',views.sejwan, name='sejwan'),
         path('idiya',views.idiya, name='idiya'),
         path('nan',views.nan, name='nan'),
]
