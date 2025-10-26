import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Avaliador(User):
    #propriedade herdadas da classe USER
    # first_name = models.CharField(_("first name"), max_length=150, blank=True)
    # last_name = models.CharField(_("last name"), max_length=150, blank=True)
    # email = models.EmailField(_("email address"), blank=True)
    # ativo = models.BooleanField(default=True)
    # is_staff (membro da equipe, permite logar na área de Administrador)

    nome = models.CharField(max_length=150, null=False, blank=False)
    telefone = models.CharField(verbose_name='Telefone', max_length=15, null=True, blank=True, help_text= 'Informe um telefone ou celular para contato')
    servidor_ifpr = models.BooleanField(verbose_name='Servidor do IFPR', default=True, help_text= 'Marque essa opção caso seja Servidor do IFPR')


    def __str__(self) -> str:
        return f'{self.nome}'

class Curso(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    nome_curso_abreviado = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    nivel = models.CharField(max_length=50, null=True, blank=True)
    modalidade = models.CharField(max_length=50, null=True, blank=True)
    turno = models.CharField(max_length=50, null=False, blank=False)
    duracao = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    carga_horaria = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(5000)])
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nome}'



class Turma(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    ano = models.IntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(datetime.date.today().year)])  # ano atual
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=False, null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nome}'


class Docente(Avaliador):
    # ativo = models.BooleanField(default=True)
    # nome = models.CharField(max_length=150, null=False, blank=False)
    # email = models.EmailField(max_length=50, null=True, blank=True)
    formacao = models.CharField(max_length=150, null=True, blank=True)
    area_tecnica = models.BooleanField(default=False)
    cursos = models.ManyToManyField(Curso)

    # def __str__(self) -> str:
    #     return f'{self.nome}'


class Aluno(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=True)
    ano_ingresso = models.IntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(datetime.date.today().year)])  # ano atual
    turma = models.ForeignKey(Turma, on_delete=models.RESTRICT, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.nome} - {self.turma}'


class Trabalho_Final(models.Model):
    class Meta:
        verbose_name = 'Projeto Final Interdisciplinar (PFI)'
        verbose_name_plural = 'Projetos Finais Interdisciplinares'

    titulo = models.CharField(max_length=250, null=False, blank=False)
    resumo = models.TextField()
    tipo = models.CharField(max_length=150, null=True, blank=True)
    ano = models.IntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(datetime.date.today().year)])  # ano atual
    autor = models.ForeignKey(Aluno, on_delete=models.RESTRICT, blank=False, null=False)
    orientador = models.ForeignKey(Docente, on_delete=models.RESTRICT, blank=False, null=False)
    coorientador = models.ForeignKey(Avaliador, related_name='Coorientador', on_delete=models.RESTRICT, blank=True, null=True)
    url = models.URLField(max_length=250, null=False, blank=False, verbose_name='URL')

    def __str__(self) -> str:
        return f'{self.titulo} - {self.autor.nome} ano: {self.ano}'


class Banca(models.Model):
    trabalho = models.ForeignKey(Trabalho_Final, on_delete=models.RESTRICT, blank=False, null=False)
    membro_banca1 = models.ForeignKey(Avaliador, related_name='membro_banca1', on_delete=models.RESTRICT, blank=False, null=False)
    membro_banca2 = models.ForeignKey(Avaliador, related_name='membro_banca2', on_delete=models.RESTRICT, blank=False, null=False)
    data_apresentacao = models.DateTimeField(null=False, blank=False)
    conceito_final = models.CharField(max_length=1, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, default='PENDENTE')
    observacao = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.trabalho.titulo} - {self.trabalho.autor.nome} ano: {self.trabalho.ano}'