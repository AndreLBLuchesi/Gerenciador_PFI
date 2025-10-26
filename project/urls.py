"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pfi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='home'), 
    path('alunos/listar/', views.ListAlunos.as_view(), name='alunos'),
    path('alunos/novo/', views.CreateAluno.as_view(), name='new_aluno'),
    path('alunos/editar/<int:pk>/', views.UpdateAluno.as_view(), name='update_aluno'),
    path('alunos/remover/<int:pk>/', views.DeleteAluno.as_view(), name='delete_aluno'),
    
    path('docentes/listar/', views.ListDocentes.as_view(), name='docentes'),
    path('docentes/novo/', views.CreateDocente.as_view(), name='new_docente'),
    path('docentes/editar/<int:pk>/', views.UpdateDocente.as_view(), name='update_docente'),
    path('docentes/remover/<int:pk>/', views.DeleteDocente.as_view(), name='delete_docente'),

    path('avaliadores/listar/', views.ListAvaliadores.as_view(), name='avaliadores'),
    path('avaliadores/novo/', views.CreateAvaliador.as_view(), name='new_avaliador'),
    path('avaliadores/editar/<int:pk>/', views.UpdateAvaliador.as_view(), name='update_avaliador'),
    path('avaliadores/remover/<int:pk>/', views.DeleteAvaliador.as_view(), name='delete_avaliador'),
    
    path('cursos/listar/', views.ListCursos.as_view(), name='cursos'),
    path('cursos/novo/', views.CreateCurso.as_view(), name='new_curso'),
    path('cursos/editar/<int:pk>/', views.UpdateCurso.as_view(), name='update_curso'),
    path('cursos/remover/<int:pk>/', views.DeleteCurso.as_view(), name='delete_curso'),
    
    path('turmas/listar/', views.ListTurmas.as_view(), name='turmas'),
    path('turmas/novo/', views.CreateTurma.as_view(), name='new_turma'),
    path('turmas/editar/<int:pk>/', views.UpdateTurma.as_view(), name='update_turma'),
    path('turmas/remover/<int:pk>/', views.DeleteTurma.as_view(), name='delete_turma'),

    path('trabalhos/listar/', views.ListTrabalhos.as_view(), name='trabalhos'),
    path('trabalhos/novo/', views.CreateTrabalho.as_view(), name='new_trabalho'),
    path('trabalhos/editar/<int:pk>/', views.UpdateTrabalho.as_view(), name='update_trabalho'),
    path('trabalhos/remover/<int:pk>/', views.DeleteTrabalho.as_view(), name='delete_trabalho'),

    path('bancas/listar/', views.ListBancas.as_view(), name='bancas'),
    path('bancas/novo/', views.CreateBanca.as_view(), name='new_banca'),
    path('bancas/editar/<int:pk>/', views.UpdateBanca.as_view(), name='update_banca'),
    path('bancas/remover/<int:pk>/', views.DeleteBanca.as_view(), name='delete_banca'),
]
