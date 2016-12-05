from django.contrib import admin
from .models import Post,Comment,Leaguetable,Gamesetinfo,Solvedproblem,Gamesetproblem

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Leaguetable)
admin.site.register(Gamesetinfo)
admin.site.register(Solvedproblem)
admin.site.register(Gamesetproblem)
