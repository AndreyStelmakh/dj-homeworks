from django.db import models


class Scope(models.Model):

    title = models.CharField(max_length=256, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['title']


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Scope, related_name='articles', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleScope(models.Model):
    scope = models.ForeignKey(Scope, related_name='scopes', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['-is_main', 'scope__title']

    def __str__(self):
        return self.scope.title

    def title(self):
        return self.scope.title
