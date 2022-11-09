from django.contrib import admin

from .models import Item, Category, Tag, Gallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb')
    list_editable = ('is_published', )
    list_display_links = ('name', )

    filter_horizontal = ('tags', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('canonical_name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ('canonical_name', )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tmb', )
