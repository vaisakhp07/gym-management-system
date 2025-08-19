# members/admin.py
from django.contrib import admin
from .models import MembershipPlan, Member, Trainer

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_months')
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'plan', 'join_date', 'active')
    list_filter = ('plan', 'active', 'join_date')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('full_name',)

    def full_name(self, obj):
        return obj.full_name()
    full_name.short_description = 'Name'

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone')
    list_filter = ('specialty',)
    search_fields = ('name', 'specialty')