import django_filters

from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Categoria, Ocorrencia

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

YES_NO_CHOICES = [('', '--------'),
                  (0, 'Não'),
                  (1, 'Sim')]


class OcorrenciaForm(ModelForm):

    tb_categoria_ID = forms.ModelChoiceField(
        label=('Tipo de Ocorrência'),
        required=True,
        queryset=Categoria.objects.all(),
        empty_label='Selecione')

    emergencia = forms.ChoiceField(
        label='Emergência?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    vitimado = forms.ChoiceField(
        label='Tem alguma vítima?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    foto = forms.ImageField(label='Fotografia',
                            required=False,
                            widget=forms.FileInput
                            )

    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 10,
                   'cols': 48,
                   'placeholder': 'Escreva aqui a descricao da ocorrencia'}))

    class Meta:
        model = Ocorrencia
        fields = ['emergencia',
                  'tb_categoria_ID',
                  'vitimado',
                  'validade',
                  'atendida',
                  'vigilante_ID',
                  'usuario_ID',
                  'hora',
                  'foto',
                  'data',
                  'latitude',
                  'longitude',
                  'descricao']

        widgets = {'atendida': forms.HiddenInput(),
                   'vigilante_ID': forms.HiddenInput(),
                   'usuario_ID': forms.HiddenInput(),
                   'validade': forms.HiddenInput()}

    def clean(self):
        cleaned_data = self.cleaned_data

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(OcorrenciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))


class ValidarOcorrenciaEditForm(ModelForm):

    emergencia = forms.ChoiceField(
        label='Emergência?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    vitimado = forms.ChoiceField(
        label='Tem alguma vítima?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    repetida = forms.ChoiceField(
        label='É repetida?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    validade = forms.ChoiceField(
        label='É válida?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    atendida = forms.ChoiceField(
        label='Foi atendida?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    class Meta:
        model = Ocorrencia
        fields = ['emergencia',
                  'tb_categoria_ID',
                  'vitimado',
                  'data',
                  'hora',
                  'latitude',
                  'longitude',
                  'validade',
                  'atendida',
                  'vigilante_ID',
                  'usuario_ID',
                  'resposta',
                  'repetida',
                  'foto',
                  'descricao']

        widgets = {'id': forms.HiddenInput(),
                   'vigilante_ID': forms.HiddenInput(),
                   'usuario_ID': forms.HiddenInput(),
                   'data': forms.HiddenInput(),
                   'hora': forms.HiddenInput(),
                   'latitude': forms.HiddenInput(),
                   'longitude': forms.HiddenInput(),
                   'descricao': forms.HiddenInput()}


class RangeWidgetOverrideDate(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'dateinput',
                                          'placeholder': 'Inicial'}),
                   forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'dateinput',
                                          'placeholder': 'Final'}))
        super(RangeWidgetOverrideDate, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)


class RangeWidgetOverrideTime(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (forms.TimeInput(format='%H:%M',
                                   attrs={'class': 'timeinput',
                                          'placeholder': 'Inicial'}),
                   forms.TimeInput(format='%H:%M',
                                   attrs={'class': 'timeinput',
                                          'placeholder': 'Final'}))
        super(RangeWidgetOverrideTime, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)


class OcorrenciaFiltro(django_filters.FilterSet):

    filter_overrides = {models.DateField: {
        'filter_class': django_filters.DateFromToRangeFilter,
        'extra': lambda f: {
            'label': '%s (%s)' % (f.verbose_name, 'Inicial - Final'),
            'widget': RangeWidgetOverrideDate}
    }}

    hora = django_filters.TimeRangeFilter(
        label='Hora (Inicial-Final)',
        widget=RangeWidgetOverrideTime)

    vitimado = django_filters.ChoiceFilter(
        label='Tem alguma vítima?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    emergencia = django_filters.ChoiceFilter(
        label='Emergência?',
        choices=YES_NO_CHOICES,
        widget=forms.Select(
            attrs={'class': 'selector'}))

    descricao = django_filters.CharFilter(
        label='Descrição (Palavras-Chave)',
        lookup_expr='icontains')

    resposta = django_filters.CharFilter(
        label='Resposta (Palavras-Chave)',
        lookup_expr='icontains')

    class Meta:
        model = Ocorrencia
        fields = ['hora',
                  'data',
                  'id',
                  'tb_categoria_ID',
                  ]

        order_by = (
            ('', 'Selecione'),
            ('dataC', 'Data - Ordem Crescente'),
            ('dataD', 'Data - Ordem Decrescente'),
        )

    order_by_mapping = {
        '': [],
        'dataC': ['data'],
        'dataD': ['-data'],
    }

    def get_order_by(self, order_value):
        if order_value in self.order_by_mapping:
            return self.order_by_mapping[order_value]
        else:
            return super(OcorrenciaFiltro,
                         self).get_order_by(order_value)

    def __init__(self, *args, **kwargs):
        super(OcorrenciaFiltro, self).__init__(*args, **kwargs)
        self.filters['id'].label = 'ID'
