from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model=ProductGallery
    extra=1
    
@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active','created_date')
    list_editable=('is_active',)
    list_filter=('product','variation_category','variation_value')
    
@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display=('product','user','subject','review','rating')




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','created_date','modified_date')
    prepopulated_fields={'slug':('product_name',)}
    inlines=[ProductGalleryInline]
    
admin.site.register(ProductGallery)