from django.contrib import admin


from .models import Payments, PaymentsDetails

# Register your models here.

admin.site.register(Payments)
admin.site.register(PaymentsDetails)