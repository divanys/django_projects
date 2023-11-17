from django.db import models


class Articles(models.Model):
    objects = None
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Текст статьи")
    date = models.DateTimeField("Дата публикации")


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural= "Статьи"

    def __str__(self):
        return self.title
