from django.views.generic import (FormView, DetailView)
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from usuario.models import Usuario
from .forms import UsuarioForm


class CriarUsuarioView(FormView):
    template_name = "usuario/cadastro_usuario.html"
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(CriarUsuarioView, self).get_context_data(
            **kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return redirect(reverse('inicio'))

    def get_initial(self):
        return {'status': 1,
                'grupo_usuario': 1}

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


class PerfilView(DetailView):
    template_name = "usuario/perfil.html"

    def get_object(self):
        if not self.request.user.is_superuser:
            return Usuario.objects.get(user_id=self.request.user.id)
        else:
            return User.objects.get(id=self.request.user.id)
