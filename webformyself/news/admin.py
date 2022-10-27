from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

# меняем отображение в админке
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'create_at', 'update_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title') # какие поля будут ссылками в админке
    search_fields = ('title', 'content')
    list_editable = ('is_published',) # возможность редактировать прямо в списке новостей
    list_filter = ('is_published', 'category') # возможность фильтрации по выбранным полям
    fields = ('title', 'category', 'content', 'photo', 'is_published', 'get_photo', 'views', 'create_at', 'update_at')
    readonly_fields = ('get_photo', 'views', 'create_at', 'update_at')
    save_on_top = True

    #вывод поля с миниатюрой фото новости
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '–'

    get_photo.short_description = 'Миниатюра' # замена названия столбца


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin) # порядок перечисления важен! сначала основную модель, затем класс ее настройки
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'