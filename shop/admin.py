from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'My Shop Administration'
admin.site.site_title = 'myshop admin'
