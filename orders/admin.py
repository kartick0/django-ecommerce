from django.contrib import admin
from .models import OrderProduct, Order, Payment
# Register your models here.
class OrderProductInline(admin.TabularInline):
    model=OrderProduct
    readonly_fields=('payment','user','product','quantity','product_price','ordered','variations')
    extra=0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('order_number','full_name','phone','email','city','order_total','tax','payment','status','is_ordered')
    list_filter=('status','is_ordered')
    search_fields=('order_number','first_name','last_name','phone','email')
    list_per_page=20
    inlines=(OrderProductInline,)
    
    
@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display=('order','ordered')
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('user','status')