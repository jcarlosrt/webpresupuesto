# Generated by Django 4.1.4 on 2023-02-28 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Procedencia', models.CharField(blank=True, choices=[('Online', 'Online'), ('OFICINA', 'Oficina'), ('ORDEN MEDICA ELECTRONICA', 'Orden Medica Electronica'), ('OTRO', 'Otro')], max_length=100, null=True)),
                ('Procedencia_key', models.IntegerField(blank=True, null=True)),
                ('IpAddress', models.CharField(blank=True, max_length=15, null=True)),
                ('StartedOn', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('SubmittedOn', models.DateTimeField(blank=True, null=True)),
                ('UserId', models.CharField(blank=True, max_length=37, null=True)),
                ('UserProvider', models.CharField(blank=True, max_length=50, null=True)),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('ClassId', models.CharField(blank=True, max_length=20, null=True)),
                ('ReferralCode', models.CharField(blank=True, max_length=10, null=True)),
                ('Language', models.CharField(blank=True, max_length=10, null=True)),
                ('SourceSiteId', models.CharField(blank=True, max_length=37, null=True)),
                ('SourceSiteDisplayName', models.CharField(blank=True, max_length=37, null=True)),
                ('ApplicationName', models.CharField(blank=True, max_length=30, null=True)),
                ('DateCreated', models.DateTimeField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=250, null=True)),
                ('ExpirationDate', models.DateTimeField(blank=True, null=True)),
                ('Web_key', models.CharField(blank=True, max_length=37, null=True)),
                ('LastModified', models.DateTimeField(blank=True, null=True)),
                ('Owner', models.CharField(blank=True, max_length=37, null=True)),
                ('PublicationDate', models.DateTimeField(blank=True, null=True)),
                ('Status', models.CharField(blank=True, max_length=30, null=True)),
                ('Title', models.CharField(blank=True, max_length=150, null=True)),
                ('Visible', models.CharField(blank=True, max_length=5, null=True)),
                ('SourceKey', models.CharField(blank=True, max_length=150, null=True)),
                ('Ingresa_el_nombre_de_tu_Isapre', models.CharField(blank=True, max_length=150, null=True)),
                ('Apellido', models.CharField(blank=True, max_length=150, null=True)),
                ('Fecha_probable_de_Hospitalizacion', models.CharField(blank=True, max_length=150, null=True)),
                ('Nombre_de_la_intervencion', models.CharField(blank=True, max_length=150, null=True)),
                ('Pasaporte', models.CharField(blank=True, max_length=150, null=True)),
                ('Apellido_Paterno', models.CharField(blank=True, max_length=200, null=True)),
                ('Seguro_complementario', models.CharField(blank=True, choices=[('Allianz', 'Allianz'), ('Best Doctors', 'Best Doctors'), ('BiceVida', 'BiceVida'), ('Bupa International', 'Bupa International'), ('Chilena Consolidada', 'Chilena Consolidada'), ('Cigna', 'Cigna'), ('Consorcio', 'Consorcio'), ('Euroamérica', 'Euroamérica'), ('Henner', 'Henner'), ('Hth Worldwide /Geoblue', 'Hth Worldwide /Geoblue'), ('International Sos', 'International Sos'), ('Mdabroad / Aetna', 'Mdabroad / Aetna'), ('Metlife', 'Metlife'), ('Sura', 'Sura'), ('Vida Cámara', 'Vida Cámara'), ('Vida Security', 'Vida Security'), ('Otro', 'Otro')], max_length=150, null=True)),
                ('Apellido_Materno', models.CharField(blank=True, max_length=150, null=True)),
                ('Telefono_movil', models.CharField(blank=True, max_length=30, null=True)),
                ('Isapre', models.CharField(blank=True, choices=[('FONASA', 'FONASA'), ('Banmédica S.A.', 'Banmédica S.A.'), ('CTC - Istel S.A.', 'CTC - Istel S.A.'), ('Chuquicamata Ltda.', 'Chuquicamata Ltda.'), ('Colmena Golden Cross S.A.', 'Colmena Golden Cross S.A.'), ('Consalud S.A.', 'Consalud S.A.'), ('Cruz del Norte Ltda', 'Cruz del Norte Ltda'), ('F.A.S.T. del Banco del Estado', 'F.A.S.T. del Banco del Estado'), ('Fundación de Salud El Teniente', 'Fundación de Salud El Teniente'), ('Isapre CruzBlanca S.A.', 'Isapre CruzBlanca S.A.'), ('Normédica S.A.', 'Normédica S.A.'), ('Nueva Masvida', 'Nueva Masvida'), ('Optima', 'Optima'), ('Particular', 'Particular'), ('Promepart Isapre', 'Promepart Isapre'), ('Río Blanco Ltda.', 'Río Blanco Ltda.'), ('San Lorenzo Ltda.', 'San Lorenzo Ltda.'), ('Sfera S.A.', 'Sfera S.A.'), ('Vida Plena S.A.', 'Vida Plena S.A.'), ('Vida Tres S.A.', 'Vida Tres S.A.'), ('Otra', 'Otra')], max_length=150, null=True)),
                ('Ingresa_el_nombre_de_tu_Seguro_Complementario', models.CharField(blank=True, max_length=150, null=True)),
                ('Adjuntar_orden_medica', models.CharField(blank=True, max_length=250, null=True)),
                ('Telefono_fijo', models.CharField(blank=True, max_length=50, null=True)),
                ('Solicitar_el_presupuesto_utilizando', models.CharField(blank=True, max_length=50, null=True)),
                ('Codigo_de_intervencion', models.CharField(blank=True, max_length=50, null=True)),
                ('RUT', models.CharField(blank=True, max_length=50, null=True)),
                ('Email_de_contacto', models.CharField(blank=True, max_length=150, null=True)),
                ('Nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('Tu_telefono_de_contacto_es', models.CharField(blank=True, max_length=50, null=True)),
                ('Fecha_de_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('Medico_tratante', models.CharField(blank=True, max_length=200, null=True)),
                ('pri_contac', models.BooleanField(blank=True, null=True)),
                ('F_primer_contac', models.DateTimeField(blank=True, null=True)),
                ('observacion_primercont', models.TextField(blank=True, max_length=500, null=True)),
                ('envio_presu', models.BooleanField(blank=True, default=False, null=True)),
                ('fecha_envio_presu', models.DateTimeField(blank=True, null=True)),
                ('observacion_envio_presu', models.TextField(blank=True, max_length=500, null=True)),
                ('fecha_y_hora_estimada_hospitalizacion_por_presu', models.DateTimeField(blank=True, null=True)),
                ('fecha_y_hora_confirmada_hospitalizacion', models.DateTimeField(blank=True, null=True)),
                ('Estado_requerimiento', models.CharField(blank=True, choices=[('PE', 'Pendiente'), ('ER', 'En espera de Respuesta'), ('EG', 'En Gestion'), ('CE', 'Cerrado')], default='PE', max_length=2, null=True)),
            ],
        ),
    ]
