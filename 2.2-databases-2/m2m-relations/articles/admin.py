from django.contrib import admin

from .models import Article, Tag, ArticleTag
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clear(self):
        for form in self.forms:
            if form.is_valid:
                form.cleaned_data
            else:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()

class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'text', 'published_at']
    ordering = ['-published_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ArticleTagInline]