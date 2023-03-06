from rest_framework.serializers import ModelSerializer
from App.post.models import Post

class PostSerialzer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['Procedencia',	'Procedencia_key',	'IpAddress',	'StartedOn',	'SubmittedOn',	'UserId',	'UserProvider',	'Username',	'ClassId',	'ReferralCode',	'Language',	'SourceSiteId',	'SourceSiteDisplayName',	'ApplicationName',	'DateCreated',	'Description',	'ExpirationDate',	'Web_key',	'LastModified',	'Owner',	'PublicationDate',	'Status',	'Title',	'Visible',	'SourceKey',	'Ingresa_el_nombre_de_tu_Isapre',	'Apellido',	'Fecha_probable_de_Hospitalizacion',	'Nombre_de_la_intervencion',	'Pasaporte',	'Apellido_Paterno',	'Seguro_complementario',	'Apellido_Materno',	'Telefono_movil',	'Isapre',	'Ingresa_el_nombre_de_tu_Seguro_Complementario',	'Adjuntar_orden_medica',	'Telefono_fijo',	'Solicitar_el_presupuesto_utilizando',	'Codigo_de_intervencion',	'RUT',	'Email_de_contacto',	'Nombre',	'Tu_telefono_de_contacto_es',	'Fecha_de_nacimiento',	'Medico_tratante'
]
