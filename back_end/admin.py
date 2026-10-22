from django.contrib import admin

# Register your models here.

from .models import ExecMember, IdentityMember, OtherMember, AboutImage

admin.site.register(ExecMember)
admin.site.register(IdentityMember)
admin.site.register(OtherMember)
admin.site.register(AboutImage)
