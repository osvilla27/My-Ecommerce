import admin_thumbnails
from django.contrib import admin

# Register your models here.
from product.models import Product, Images, Variants, Color, Size


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','image_tag'] #'category'
    list_filter = ['price', 'amount', 'keywords'] #'category'
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline,ProductVariantsInline]
    prepopulated_fields = {'slug': ('title',)}


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','code','color_tag']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','color','size','price','quantity','image_tag']


admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)
