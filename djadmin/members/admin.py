from django.contrib import admin

# Register your models here.
from .models import Member

def custom_action(modeladmin, request, queryset):
    # Your custom action logic here
    queryset.update(firstname='custom_name')

custom_action.short_description = "Custom Action Description"

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    change_list_template = 'admin/custom_change_member_list.html'
    actions = [custom_action]

# def get_actions(self, request):
#     actions = super(MemberAdmin, self).get_actions(request)
#     actions['custom_action'] = (self.custom_action, 'custom_action', 'Custom Action Description')
#     return actions


admin.site.register(Member, MemberAdmin)