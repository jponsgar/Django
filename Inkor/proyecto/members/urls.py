from django.urls import path
"""Hay dos formas de importar los views:"""
from . import views         # importación desde la carpeta actual
# from members import views # importación indicando carpeta de APP

urlpatterns = [
  # path("", <view_aqui>, name="<nombre (opcional)>"),
  path('members/', views.members, name='members'),
]
