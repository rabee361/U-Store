from django.contrib import admin
from .models import *

@admin.register(MerchantCurrency)
class MerchantCurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant', 'name', 'symbol', 'parts','parts_name']
    search_fields = ['name', 'symbol', 'merchant__user__email']
    list_filter = ['merchant', 'name', 'symbol']
    ordering = ['merchant', 'name']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant', 'merchant__user')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant', 'en_name', 'ar_name', 'slug']
    search_fields =['en_name', 'ar_name', 'merchant__user__email']
    list_filter = ['merchant']
    ordering = ['merchant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant', 'merchant__user')


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'designer', 'price', 'rating']


@admin.register(Plan)
class PlansAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(MerchantPlan)
class MerchantPlansAdmin(admin.ModelAdmin):
    list_display = ['id', 'plan', 'merchant']


@admin.register(StoreTheme)
class StoreThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'primary', 'secondary', 'tertiary']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'merchant', 'category', 'code', 'en_name', 'ar_name',
        'price', 'current_quantity', 'displayed', 'isActive', 'isDeleted'
    ]
    search_fields = [
        'code', 'en_name', 'ar_name', 'barcode', 'description',
        'merchant__user__email', 'category__name'
    ]
    list_filter = [
        'merchant', 'category', 'displayed', 'isActive', 'isDeleted',
        'shipped', 'tax', 'weight_unit', 'cost_currency'
    ]
    ordering = ['merchant', 'category', 'en_name']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'merchant', 'merchant__user', 'category', 'weight_unit', 'cost_currency'
        )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant', 'name', 'link']
    search_fields = ['name', 'link', 'merchant__user__email']
    list_filter = ['merchant']
    ordering = ['merchant', 'name']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant', 'merchant__user')


@admin.register(MerchantSocial)
class MerchantSocialAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant', 'facebook', 'twitter', 'instagram', 'telegram', 'email']
    search_fields = ['merchant__user__email', 'facebook', 'twitter', 'instagram', 'telegram', 'email']
    list_filter = ['merchant']
    ordering = ['merchant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant', 'merchant__user')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'merchant', 'name', 'country', 'city',
        'neighborhood', 'street', 'selling_point'
    ]
    search_fields = [
        'name', 'country', 'city', 'neighborhood', 'street',
        'selling_point', 'merchant__user__email'
    ]
    list_filter = ['merchant', 'country', 'city']
    ordering = ['merchant', 'country', 'city', 'name']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant', 'merchant__user')
