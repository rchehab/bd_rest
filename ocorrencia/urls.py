from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import (CriarOcorrenciaView, DescricaoOcorrenciaView,
                    ListaOcorrenciasView,
                    ListaValidacaoView, ValidarOcorrenciaEditView,
                    MinhasOcorrenciasView)

urlpatterns = [
    url(r'^ocorrencias/$',
        ListaOcorrenciasView.as_view(), name='lista_ocorrencias'),

    url(r'^ocorrencias/criar-ocorrencia/$',
        CriarOcorrenciaView.as_view(), name='criar_ocorrencia'),

    url(r'^ocorrencias/(?P<pk>\d+)$',
        DescricaoOcorrenciaView.as_view(), name='ver_ocorrencia'),

    url(r'^ocorrencias/validar$',
        ListaValidacaoView.as_view(), name='lista_validacao'),

    url(r'^ocorrencias/(?P<pk>\d+)/validar$',
        ValidarOcorrenciaEditView.as_view(), name='validar_ocorrencia'),

    url(r'^ocorrencias/minhas_ocorrencias/$',
        MinhasOcorrenciasView.as_view(), name='minhas_ocorrencias'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
