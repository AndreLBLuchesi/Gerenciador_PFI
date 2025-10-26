
from django import forms

from pfi import models

class DocenteForm(forms.ModelForm):
    
    """
    veja a documentação
    https://docs.djangoproject.com/en/5.1/ref/forms/widgets/
    """
    class Meta:
        model = models.Docente
        
        fields = ['is_active','nome', 'email', 'username', 'password', 'telefone','formacao', 'area_tecnica', 'cursos']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'type': 'hidden'}),
            'nome': forms.TextInput(attrs={'class': 'form-group form-control', "title": "Informe o nome", "placeholder": "Informe o nome"}),
            'username': forms.TextInput(attrs={'class': 'form-group form-control', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-group form-control', 'autocomplete': 'new-password' }),
            'email': forms.EmailInput(attrs={'class': 'form-group form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-group form-control', "placeholder": "(XX) XXXXX-XXXX"}),
            'formacao': forms.TextInput(attrs={'class': 'form-group form-control'}),
            'area_tecnica': forms.CheckboxInput(attrs={'class': ' form-group'})
            
        }
    
    # Editar Fields 
    # veja a documentação: https://docs.djangoproject.com/en/5.1/ref/forms/fields/
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].disabled = True
        self.fields['is_active'].checked = True
        self.fields['area_tecnica'].label = 'Faz parte da área técnica? '

class AvaliadorForm(forms.ModelForm):
    class Meta:
        model = models.Avaliador

        fields = ['is_active', 'nome', 'email', 'username', 'password', 'telefone', 'servidor_ifpr']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'type': 'hidden'}),
            'nome': forms.TextInput(
                attrs={'class': 'form-group form-control', "title": "Informe o nome", "placeholder": "Informe o nome"}),
            'username': forms.TextInput(attrs={'class': 'form-group form-control', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-group form-control', 'autocomplete': 'new-password'}),
            'email': forms.EmailInput(attrs={'class': 'form-group form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-group form-control', "placeholder": "(XX) XXXXX-XXXX"}),
            'formacao': forms.TextInput(attrs={'class': 'form-group form-control'}),
            'servidor_ifpr': forms.CheckboxInput(attrs={'class': ' form-group', 'checked': 'checked'}),

        }

    # Editar Fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].disabled = True
        self.fields['is_active'].checked = True
        
class AlunoForm(forms.ModelForm):
    class Meta:
        model = models.Aluno
        fields = "__all__"
        widgets = {
            'ativo': forms.CheckboxInput(attrs={'type': 'hidden', 'checked': 'checked'}),
            'nome': forms.TextInput( attrs={'class': 'form-group form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-group form-control'}),
            'ano_ingresso': forms.Select(attrs={'class': 'form-group form-control'},
                                choices={2025: '2025', 2024: '2024', 2023: '2023', 2022: '2022', 2021: '2021', 2020: '2020'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['turma'].widget.attrs = {'class': 'form-group form-select'}
    

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"
        widgets = {
            'ativo': forms.CheckboxInput(attrs={'type': 'hidden'}),
            'nome': forms.TextInput( attrs={'class': 'form-group form-control'}),
            'nome_curso_abreviado': forms.TextInput( attrs={'class': 'form-group form-control'}),
            'descricao': forms.Textarea( attrs={'class': 'form-group form-control', "cols": "40", "rows": "5"}),
            'duracao': forms.NumberInput(attrs={'class': 'form-group form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'MEDIO':'Ensino Médio', 'SUPERIOR': 'Ensino Superior', 'POS-GRADUACAO': 'Pós-Graduação' }),
            'modalidade': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'PRESENCIAL':'Presencial', 'EAD': 'EAD' }),
            'turno': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'MATUTINO':'Matutino', 'VESPERTINO': 'Vespertino', 'PARCIAL DIURNO': 'Parcial Diurno', 'NOTURNO': 'Noturno', 'INTEGRAL': 'Integral' }),
            'ano': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6' }),
            'carga_horaria': forms.NumberInput( attrs={'class': 'form-group form-control'})
        }
 
    # Editar Fields 
    # veja a documentação: https://docs.djangoproject.com/en/5.1/ref/forms/fields/
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ativo'].disabled = True
        self.fields['descricao'].label = 'Descrição'
        self.fields['nivel'].label = 'Nível'
        self.fields['duracao'].label = 'Duração'
        self.fields['carga_horaria'].label = 'Carga Horária'
 

class TurmaForm(forms.ModelForm):
    
    class Meta:
        model = models.Turma
        fields = '__all__'
        widgets = {
            'ativo': forms.CheckboxInput(attrs={'type': 'hidden'}),
            'nome': forms.TextInput( attrs={'class': 'form-group form-control'}),
            'ano': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={2025:'2025', 2024: '2024', 2023: '2023', 2022:'2022', 2021:'2021', 2020:'2020'}),
            # 'curso': forms.ModelChoiceField(queryset=models.Curso.objects.filter(ativo=False)),
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['ativo'].disabled = True
        self.fields['curso'].queryset= models.Curso.objects.filter(ativo=True)
        self.fields['curso'].widget.attrs={'class': 'form-group form-select'}
        
class TrabalhoFinalForm(forms.ModelForm):
    class Meta:
        model = models.Trabalho_Final
        fields = "__all__"
        widgets = {
            'titulo': forms.TextInput( attrs={'class': 'form-group form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-group form-control', "cols": "40", "rows": "5"}),
            'tipo': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'WEBSITE':'WEBSITE', 'DESKTOP':'Sistema Desktop', 'MOBILE':'Aplicativo Mobile', 'ROBOTICA':'Projeto de Robótica', 'Outro':'Outro' }),
            'ano': forms.Select(attrs={'class': 'form-group form-control'},
                                choices={2025:'2025', 2024: '2024', 2023: '2023', 2022:'2022', 2021:'2021', 2020:'2020'}),
            'url': forms.URLInput(attrs={'class': 'form-group form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['autor'].queryset = models.Aluno.objects.filter(ativo=True)
        self.fields['autor'].widget.attrs = {'class': 'form-group form-select'}
        self.fields['orientador'].queryset = models.Docente.objects.filter(is_active=True)
        self.fields['orientador'].widget.attrs = {'class': 'form-group form-select'}
        self.fields['coorientador'].queryset = models.Avaliador.objects.filter(is_active=True, servidor_ifpr=True)
        self.fields['coorientador'].widget.attrs = {'class': 'form-group form-select'}
        self.fields['coorientador'].widget.attrs = {'class': 'form-group form-select'}


class BancaForm(forms.ModelForm):
    class Meta:
        model = models.Banca
        fields = '__all__'
        widgets = {
            'data_apresentacao' : forms.DateTimeInput(attrs={'class': 'form-group form-control', 'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'class': 'form-group form-control', "cols": "40", "rows": "5"}),
            'conceito_final': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'': 'Selecione o Conceito','A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}),
            'status': forms.Select(attrs={'class': 'form-group form-select'},
                                choices={'PENDENTE': 'PENDENTE', 'FINALIZADO': 'FINALIZADO'}),
            # 'curso': forms.ModelChoiceField(queryset=models.Curso.objects.filter(ativo=False)),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['trabalho'].queryset = models.Trabalho_Final.objects.filter().order_by('ano')
        self.fields['trabalho'].widget.attrs = {'class': 'form-group form-select'}
        self.fields['membro_banca1'].queryset = models.Avaliador.objects.filter().order_by('nome')
        self.fields['membro_banca1'].widget.attrs = {'class': 'form-group form-select'}
        self.fields['membro_banca2'].queryset = models.Avaliador.objects.filter().order_by('nome')
        self.fields['membro_banca2'].widget.attrs = {'class': 'form-group form-select'}