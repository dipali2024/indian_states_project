from django.contrib import admin
from indian_states.models import State
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display=('id','name','population','language','capital')

admin.site.register(State,StateAdmin)