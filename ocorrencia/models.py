from django.db import models

class Categoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    descricao = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tb_categoria'

    def __str__(self):
        return ('%(descricao)s') % {
            'descricao': self.descricao}

class Local(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(max_length=45, blank=False, null=False)
    descricao = models.CharField(max_length=45, blank=False, null=False)
    pai = models.IntegerField(db_column ='pai', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_local'

    def __str__(self):
        return ('%(descricao)s') % {
            'descricao': self.descricao}


class Ocorrencia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    data = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(max_length=90, blank=True, null=True)
    validade = models.BooleanField(null=False, default=False)
    atendida = models.BooleanField(null=False, default=False)
    emergencia = models.BooleanField(null=False, default=False)
    vitimado = models.BooleanField()
    repetida = models.BooleanField()
    resposta = models.CharField(max_length=45, blank=True, null=True)
    usuario_ID = models.IntegerField(db_column='usuario_ID', blank=False, null=False)
    vigilante_ID = models.IntegerField(db_column='vigilante_ID')
    tb_categoria_ID = models.ForeignKey(Categoria, db_column='tb_categoria_ID')
    tb_local_ID = models.ForeignKey(Local, db_column='tb_local_ID')

    class Meta:
        verbose_name = ('Ocorrência')
        verbose_name_plural = ('Ocorrências')
        unique_together = (("data", "id"),)
        managed = False
        db_table = 'tb_ocorrencia'

    def __str__(self):
        return ('%(data)s - %(id)s') % {
            'data': self.data, 'id': self.id}