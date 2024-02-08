from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Formulario/', views.mi_formulario, name="Formulario"),
    path('ProbandoTemplate/', views.probandoTemplate, name="Probando Template"),
    path('Carga/', views.carga, name="Carga"),
    path('ProbandoBootstrap/', views.probando_bootstrap, name="Probando Booststrap"),
]
