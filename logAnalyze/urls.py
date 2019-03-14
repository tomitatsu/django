from django.urls import path

from . import views

app_name='logAnalyze'

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/<path:url>', views.analyze, name='analyze'),
    path('<path:url>/results/', views.results, name='results'),
]
