from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        already_has_main = False
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main', False)
            if already_has_main is True and is_main is True:
                raise ValidationError('В качестве основного может быть выбран только один раздел')
            if is_main:
                already_has_main = True
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    pass
