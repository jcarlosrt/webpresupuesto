from django.contrib import admin
from App.cliente.models import Basecliente
from App.cliente.models import prevision
from App.cliente.models import estadocivil
from App.cliente.models import comuna
from App.cliente.models import region




admin.site.register(Basecliente)
admin.site.register(prevision)
admin.site.register(estadocivil)
admin.site.register(comuna)
admin.site.register(region)

# Register your models here.
