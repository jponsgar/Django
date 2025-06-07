from django.urls import path
"""Hay dos formas de importar los views:"""
from . import views         # importación desde la carpeta actual
# from members import views # importación indicando carpeta de APP

urlpatterns = [
  # path("", <view_aqui>, name="<nombre (opcional)>"),
  path('', views.index, name='index'),
  path('members/', views.members, name='members'),
  # path que recibe un entero (int) para mostrar un member de la lista por id:
  path('members/<int:id>', views.members_detail, name='members-detail'),
]
