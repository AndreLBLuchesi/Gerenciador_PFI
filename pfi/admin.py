from django.contrib import admin

from pfi.models import Aluno, Curso, Docente, Trabalho_Final, Turma, Avaliador, Banca


# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'turno', 'carga_horaria')
    ordering = 'nome',
    search_fields = ('id', 'nome', 'turno')
    list_display_links = ('id', 'nome')
    list_per_page = 25
    list_max_show_all = 200
    
@admin.register(Turma)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'curso')
    ordering = 'ano',
    search_fields = ('id', 'nome', 'ano', 'curso')
    list_display_links = ('id', 'nome')
    list_per_page = 25
    list_max_show_all = 200

@admin.register(Avaliador)
class AvaliadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email' )
    ordering = 'nome',
    search_fields = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'formacao')
    ordering = 'nome',
    search_fields = ('id', 'nome', 'email', 'formacao')
    list_display_links = ('id', 'nome')
    list_per_page = 25
    list_max_show_all = 200


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'turma')
    ordering = '-id',
    search_fields = ('id', 'nome', 'email', 'turma')
    list_display_links = ('id', 'nome')
    list_per_page = 25
    list_max_show_all = 200

@admin.register(Trabalho_Final)
class Trabalho_FinalAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'orientador', 'ano')
    ordering = '-id',
    search_fields = ('id', 'titulo', 'autor', 'orientador', 'ano')
    list_display_links = ('id', 'titulo')
    list_per_page = 25
    list_max_show_all = 200

@admin.register(Banca)
class BancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabalho', 'membro_banca1', 'membro_banca1', 'data_apresentacao')
    ordering = '-id',
    # search_fields = ('id', 'pfi.Banca.titulo', 'pfi.Banca.autor', 'pfi.Banca.orientador', 'ano')
    list_display_links = ('id', )
