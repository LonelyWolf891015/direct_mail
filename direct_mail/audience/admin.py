from django.contrib import admin
from .models import Audience
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_Factory
# Register your models here.
@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    pass
