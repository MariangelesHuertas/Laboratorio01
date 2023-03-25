from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path('', views.index, name='index'),
    # ex: localhost:8080/polls/5/
    path('<int:pregunta_id>/', views.suma, name='suma'),
    # ex: localhost:8080/polls/5/results/
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
]

