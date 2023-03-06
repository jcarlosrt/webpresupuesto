from django.contrib import admin
from App.post.models import Post
from App.seguiweb.models import Eventos
from App.seguiweb.models import Seguimientos
# Register your models here.

admin.site.register(Post)

admin.site.register(Eventos)
admin.site.register(Seguimientos)


#from App.post.models import Post
#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    list_display = [Post]