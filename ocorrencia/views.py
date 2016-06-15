from django.views.generic import (FormView, ListView, DetailView,
                                  UpdateView)
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.urlresolvers import reverse, reverse_lazy
from django_filters.views import FilterView
from django.shortcuts import redirect

from unb_alerta.utils import make_pagination

from usuario.models import Usuario

from .models import Ocorrencia

from .forms import OcorrenciaForm, ValidarOcorrenciaEditForm, OcorrenciaFiltro


class ListaOcorrenciasView(LoginRequiredMixin, FilterView):
    model = Ocorrencia
    filterset_class = OcorrenciaFiltro
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListaOcorrenciasView,
                        self).get_context_data(**kwargs)

        paginator = context['paginator']
        page_obj = context['page_obj']

        context['page_range'] = make_pagination(
            page_obj.number, paginator.num_pages)

        return context

    def get(self, request, *args, **kwargs):
        super(ListaOcorrenciasView, self).get(request)

        # Se a pesquisa estiver quebrando com a paginação
        # Olhe esta função abaixo
        # Provavelmente você criou um novo campo no Form/FilterSet
        # Então a ordem da URL está diferente
        data = self.filterset.data
        if (data and data.get('tb_categoria_ID') is not None):
            url = "&" + str(self.request.environ['QUERY_STRING'])
            if url.startswith("&page"):
                ponto_comeco = url.find('tb_categoria_ID=') - 1
                url = url[ponto_comeco:]
        else:
            url = ''

        self.filterset.form.fields['o'].label = 'Ordenação'

        queryset = self.object_list.filter(
            atendida=True,
            validade=True).distinct()

        context = self.get_context_data(filter=self.filterset,
                                        object_list=queryset,
                                        filter_url=url,
                                        numero_res=len(self.object_list)
                                        )

        return self.render_to_response(context)


class CriarOcorrenciaView(LoginRequiredMixin, FormView):
    template_name = "ocorrencia/nova_ocorrencia.html"
    form_class = OcorrenciaForm

    def get_context_data(self, **kwargs):

        context = super(CriarOcorrenciaView, self).get_context_data(
            **kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return redirect(reverse('lista_ocorrencias'))

    def get_initial(self):
        if self.request.user.is_superuser is False:
            usuario = Usuario.objects.get(user_id=self.request.user.id)
            return {'validade': False,
                    'atendida': False,
                    'vigilante_ID': 1,
                    'usuario_ID': usuario.id,
                    'repetida': False}
        else:
            return {'validade': False,
                    'atendida': False,
                    'vigilante_ID': 1,
                    'usuario_ID': self.request.user.id,
                    'repetida': False}

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            ocorrencia = form.save(commit=False)

            if 'foto' in request.FILES:
                ocorrencia.foto = request.FILES['foto']
            ocorrencia.save()
            return self.form_valid(form)
        else:
            mensagem = "Formulário Inválido"
            messages.add_message(request, messages.ERROR, mensagem)
            return self.render_to_response(
                {'form': form})


class ListaValidacaoView(PermissionRequiredMixin, ListView):
    template_name = "ocorrencia/validacao_list.html"
    model = Ocorrencia
    queryset = Ocorrencia.objects.filter(atendida=False).order_by('-id')
    paginate_by = 10
    permission_required = {'ocorrencia.change_ocorrencia'}

    def get_context_data(self, **kwargs):
        context = super(ListaValidacaoView, self).get_context_data(**kwargs)

        if not context.get('object_list'):
            context['vazio'] = True

        paginator = context['paginator']
        page_obj = context['page_obj']

        context['page_range'] = make_pagination(
            page_obj.number, paginator.num_pages)
        return context


class ValidarOcorrenciaEditView(PermissionRequiredMixin, UpdateView):
    template_name = "ocorrencia/validacao_ocorrencia.html"
    form_class = ValidarOcorrenciaEditForm
    model = Ocorrencia
    success_url = reverse_lazy('lista_ocorrencias')
    permission_required = {'ocorrencia.change_ocorrencia'}

    def get_context_data(self, **kwargs):

        context = super(ValidarOcorrenciaEditView, self).get_context_data(
            **kwargs)
        return context

    def get_initial(self):
        if self.request.user.is_superuser is False:
            usuario = Usuario.objects.get(user_id=self.request.user.id)
            o = Ocorrencia.objects.get(id=self.kwargs['pk'])
            return {'vigilante_ID': usuario.id,
                    'emergencia': o.emergencia,
                    'atendida': o.atendida,
                    'validade': o.atendida,
                    'repetida': o.repetida,
                    'vitimado': o.vitimado,
                    'foto': o.foto,
                    'descricao': o.descricao}
        else:
            return {'vigilante_ID': 1}

    def form_valid(self, form):
        ocorrencia = form.instance
        ocorrencia.id = self.kwargs['pk']
        ocorrencia.save()

        if form.data.get('repetida') == 'True':
            Ocorrencia.objects.get(id=ocorrencia.id).delete()

        return redirect(reverse('lista_ocorrencias'))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            mensagem = "Formulário Inválido"
            messages.add_message(request, messages.ERROR, mensagem)
            return self.render_to_response(
                {'form': form})


class DescricaoOcorrenciaView(DetailView):
    template_name = "ocorrencia/descricao_ocorrencia.html"

    def get_queryset(self):
        pk = self.kwargs['pk']
        ocorrencia = Ocorrencia.objects.filter(id=pk)

        return ocorrencia


class MinhasOcorrenciasView(LoginRequiredMixin, ListView):
    template_name = "ocorrencia/minhas_ocorrencias.html"
    model = Ocorrencia
    queryset = Ocorrencia.objects.filter(
        validade=True,
        atendida=True).order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MinhasOcorrenciasView, self).get_context_data(**kwargs)

        if not context.get('object_list'):
            context['vazio'] = True

        paginator = context['paginator']
        page_obj = context['page_obj']

        context['page_range'] = make_pagination(
            page_obj.number, paginator.num_pages)
        return context
