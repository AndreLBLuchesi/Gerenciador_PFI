from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q, QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from pfi.forms import AlunoForm, CursoForm, DocenteForm, TrabalhoFinalForm, TurmaForm, AvaliadorForm, BancaForm
from pfi.models import Aluno, Curso, Docente, Trabalho_Final, Turma, Avaliador, Banca

from django.db.models.functions import Lower

# Create your views here.

def pagina_inicial(request):
    return render(request, 'index.html')


class ListAlunos(ListView):
    template_name = 'aluno_list.html'
    model = Aluno
    queryset = Aluno.objects.all().order_by('nome')
    context_object_name = 'alunos'
    extra_context = {'form_titulo': 'Cadastro de Alunos'}

    def get_queryset(self):
        return Aluno.objects.all().order_by(Lower('nome'))
        # resultado = sorted(Aluno.objects.all(), cmp=lambda a,b: locale.strcoll(a.nome, b.nome)) #remover acentuação
    
class CreateAluno(CreateView):
    form_class = AlunoForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('alunos')
    
    # Sobrescreve o metodo que cria a variável de contexto (enviada na requisição HTTP)
    def get_context_data(self, **kwargs):
        ctx = super(CreateAluno, self).get_context_data(**kwargs)
        # adicionando informação a variável de contexto
        ctx['form_titulo'] = 'Adicionar Aluno'
        return ctx

class UpdateAluno(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('alunos')
    
    # Sobrescreve o metodo que cria a variável de contexto (enviada na requisição HTTP)
    def get_context_data(self, **kwargs):
        ctx = super(UpdateAluno, self).get_context_data(**kwargs)
        ctx['form_titulo'] = 'Editar Aluno'
        return ctx


class DeleteAluno(DeleteView):
    model = Aluno
    template_name = 'confirm.html'
    success_url = reverse_lazy('alunos')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Remover Aluno', 'entidade': 'Aluno'}
    
        

class ListDocentes(ListView):
    template_name = 'docente_list.html'
    model = Docente
    queryset = Docente.objects.all().order_by(Lower('nome'))
    context_object_name = 'docentes'
    extra_context = {'form_titulo':'Cadastro de Docentes'}
    
    
class CreateDocente(CreateView):
    form_class = DocenteForm
    model = Docente
    template_name = 'formulario.html'
    success_url = reverse_lazy('docentes')    
    extra_context = {'form_titulo':'Cadastrar Docente'}

    def form_valid(self, form):
        # 'commit=False' impede o salvamento imediato no banco
        self.object:Docente = form.save(commit=False)
        self.object.set_password(self.object.password)
        print(self.object.password)
        return super().form_valid(form)  # Agora ele salva e redireciona


class UpdateDocente(UpdateView):
    form_class = DocenteForm
    template_name = 'formulario.html'
    model = Docente
    success_url = reverse_lazy('docentes')
    extra_context = {'form_titulo':'Editar Docente'}

    def form_valid(self, form):
        # 'commit=False' impede o salvamento imediato no banco
        self.object:Docente = form.save(commit=False)
        self.object.set_password(self.object.password)
        print(self.object.password)
        return super().form_valid(form)  # Agora ele salva e redireciona


class DeleteDocente(DeleteView):
    model = Docente
    template_name = 'confirm.html'
    success_url = reverse_lazy('docentes')
    context_object_name = 'registro'
    extra_context = {'form_titulo':'Remover Docente','entidade': 'Docente'}

class ListAvaliadores(ListView):
    template_name = 'avaliador_list.html'
    model = Avaliador
    queryset = Avaliador.objects.filter(is_active = True, docente__isnull = True).order_by(Lower('nome'))
    ordering = ['nome']
    context_object_name = 'avaliadores'
    extra_context = {'form_titulo':'Cadastro de Avaliadores'}

class CreateAvaliador(CreateView):
    form_class = AvaliadorForm
    model = Avaliador
    template_name = 'formulario.html'
    success_url = reverse_lazy('avaliadores')
    extra_context = {'form_titulo':'Cadastrar Avaliador'}

    def form_valid(self, form):
        # 'commit=False' impede o salvamento imediato no banco
        self.object:Avaliador = form.save(commit=False)
        self.object.set_password(self.object.password)
        return super().form_valid(form)  # Agora ele salva e redireciona


class UpdateAvaliador(UpdateView):
    form_class = AvaliadorForm
    template_name = 'formulario.html'
    model = Avaliador
    success_url = reverse_lazy('avaliadores')
    extra_context = {'form_titulo':'Editar Avaliador'}

    def form_valid(self, form):
        # 'commit=False' impede o salvamento imediato no banco
        self.object:Avaliador = form.save(commit=False)
        self.object.set_password(self.object.password)
        return super().form_valid(form)  # Agora ele salva e redireciona


class DeleteAvaliador(DeleteView):
    model = Avaliador
    template_name = 'confirm.html'
    success_url = reverse_lazy('avaliadores')
    context_object_name = 'registro'
    extra_context = {'form_titulo':'Remover Avaliador','entidade': 'Avaliador'}

class ListTrabalhos(ListView):
    template_name = 'trabalho_final_list.html'
    model = Trabalho_Final
    queryset = Trabalho_Final.objects.all().order_by('ano', Lower('autor__nome'))
    # ordering = ['ano', 'descricao']
    context_object_name = 'trabalhos'
    extra_context = {'form_titulo': 'Cadastro de Trabalhos Finais (PFI)'}

    def get_queryset(self):
        filter_val = self.request.GET.get('pesquisar', '')
        return Trabalho_Final.objects.filter(Q(titulo__contains=filter_val) | Q(autor__nome__contains=filter_val) | Q(orientador__nome__icontains=filter_val)).order_by('ano',  Lower('autor__nome'))
    
class CreateTrabalho(CreateView):
    form_class = TrabalhoFinalForm
    model = Trabalho_Final
    template_name = 'formulario.html'
    success_url = reverse_lazy('trabalhos')
    extra_context = {'form_titulo': 'Cadastrar Trabalho'}

    
class UpdateTrabalho(UpdateView):
    model = Trabalho_Final
    form_class = TrabalhoFinalForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('trabalhos')
    extra_context = {'form_titulo': 'Editar Trabalho'}

    
class DeleteTrabalho(DeleteView):
    model = Trabalho_Final
    template_name = 'confirm.html'
    success_url = reverse_lazy('trabalhos')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Remover Trabalho', 'entidade': 'Trabalho'}
    
class ListCursos(ListView):
    template_name = 'cursos.html'
    model = Curso
    queryset = Curso.objects.all().order_by(Lower('nome'))
    context_object_name = 'cursos'
    extra_context = {'form_titulo':'Cadastro de Cursos'}
    
class CreateCurso(CreateView):
    form_class = CursoForm
    model = Curso
    template_name = 'formulario.html'
    success_url = reverse_lazy('cursos')
    extra_context = {'form_titulo':'Cadastrar Curso'}

class UpdateCurso(UpdateView):
    template_name = 'formulario.html'
    model = Curso
    form_class = CursoForm
    success_url = reverse_lazy('cursos')
    extra_context = {'form_titulo':'Editar Curso'}

class DeleteCurso(DeleteView):
    model = Curso
    template_name = 'confirm.html'
    success_url = reverse_lazy('cursos')
    context_object_name = 'registro'
    extra_context = {'form_titulo':'Remover Curso', 'entidade': 'o curso'}


class ListTurmas(ListView):
    template_name = 'page_list.html'
    model = Turma
    queryset = Turma.objects.filter(ativo = True).order_by( 'ano', 'curso__nome')
    context_object_name = 'turmas'
    ordering = ['-ano', 'nome']
    paginate_by = 25
    context_object_name = 'itens'
    extra_context = {'form_titulo':'Cadastro de Turmas'}
    #propriedades adicionadas
    fields = ['Nome', 'Curso', 'Ano', 'Ações']
    label_add_btn = 'Nova Turma'
    url_add_btn = 'new_turma'
    
   
    
class CreateTurma(CreateView): 
    form_titulo = 'Adicionar Turma'
    form_class = TurmaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('turmas')
    extra_context = {'form_titulo':'Cadastrar Turma'}

class UpdateTurma(UpdateView):
    template_name = 'formulario.html'
    model = Turma
    form_class = TurmaForm
    success_url = reverse_lazy('turmas')
    extra_context = {'form_titulo':'Editar Turma'}

class DeleteTurma(DeleteView):
    model = Turma
    template_name = 'confirm.html'
    success_url = reverse_lazy('turmas')
    context_object_name = 'registro'
    extra_context = {'form_titulo':'Remover Turma', 'entidade': 'a turma'}


class ListBancas(ListView):
    template_name = 'banca_list.html'
    model = Banca
    queryset = Banca.objects.all().order_by(Lower('trabalho__autor__nome'))
    context_object_name = 'bancas'
    extra_context = {'form_titulo': 'Cadastro de Bancas'}

    def get_queryset(self):
        filter_val = self.request.GET.get('pesquisar', '')
        return Banca.objects.filter(Q(trabalho__titulo__contains=filter_val) | Q(trabalho__autor__nome__contains=filter_val) | Q(
            trabalho__orientador__nome__contains=filter_val)).order_by(Lower('trabalho__autor__nome'))


class CreateBanca(CreateView):
    form_class = BancaForm
    model = Banca
    template_name = 'formulario.html'
    success_url = reverse_lazy('bancas')
    extra_context = {'form_titulo': 'Cadastrar Banca'}


class UpdateBanca(UpdateView):
    model = Banca
    form_class = BancaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('bancas')
    extra_context = {'form_titulo': 'Editar Banca'}


class DeleteBanca(DeleteView):
    model = Banca
    template_name = 'confirm.html'
    success_url = reverse_lazy('bancas')
    context_object_name = 'registro'
    extra_context = {'form_titulo': 'Remover Banca', 'entidade': 'Banca'}

class ListAgendaBanca(ListView):
    template_name = 'calendario_bancas.html'
    model = Banca
    context_object_name = 'bancas'
    extra_context = {'form_titulo': 'Agenda de Apresentações do PFI'}

    def get_queryset(self):
        filter_val = self.request.GET.get('pesquisar', '')
        return Banca.objects.filter(Q(trabalho__titulo__contains=filter_val) | Q(trabalho__autor__nome__contains=filter_val) | Q(
            trabalho__orientador__nome__contains=filter_val)).order_by(Lower('trabalho__autor__nome')).order_by('data_apresentacao')

    # Sobrescreve o metodo que cria a variável de contexto (enviada na requisição HTTP)
    def get_context_data(self, **kwargs):
        # bancas = Banca.objects.filter().order_by('data_apresentacao')
        filter_val = self.request.GET.get('pesquisar', '')
        bancas = Banca.objects.filter(
            Q(trabalho__titulo__contains=filter_val) | Q(trabalho__autor__nome__contains=filter_val) | Q(
                trabalho__orientador__nome__contains=filter_val) | Q(membro_banca1__nome__contains=filter_val)
                | Q(membro_banca2__nome__contains=filter_val)).order_by(Lower('trabalho__autor__nome')).order_by(
            'data_apresentacao')
        dias = bancas.values_list('data_apresentacao', flat=True)
        dias_diferentes: list = []
        cont = -1

        for b in bancas:
            if len(dias_diferentes) > 0:
                if b.data_apresentacao.day != dias[cont].day:
                    dias_diferentes.append(True)
                else:
                    dias_diferentes.append(False)
            else:
                dias_diferentes.append(True)
            cont += 1

        combined_data = []
        for i in range(len(dias_diferentes)):
            combined_data.append((bancas[i], dias_diferentes[i]))

        ctx = super(ListAgendaBanca, self).get_context_data(**kwargs)
        ctx['dados'] = combined_data
        return ctx