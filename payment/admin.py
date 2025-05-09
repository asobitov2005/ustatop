from django.contrib import admin
from payment.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'status')
    list_filter = ('status', 'payment_method', 'amount', 'user')
    date_hierarchy = 'date'
    search_fields = ('user', 'amount', 'date')


admin.site.register(Payment, PaymentAdmin)
