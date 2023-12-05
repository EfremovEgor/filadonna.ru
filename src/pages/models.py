from django.db import models


class Image(models.Model):
    name = models.CharField(("Название"), max_length=255)
    image = models.ImageField(
        ("Картинка"),
        upload_to="images",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ["created_date"]

    def __str__(self):
        return self.name


class BaseImageWithText(models.Model):
    overlay_text = models.CharField(("Текст"), max_length=255)
    image = models.ForeignKey(
        Image, verbose_name=("Картинка"), on_delete=models.CASCADE
    )
    link = models.CharField(("Ссылка"), max_length=255)

    class Meta:
        abstract = True


class IndexSliderImage(BaseImageWithText):
    index = models.IntegerField(("Порядковый номер"))

    class Meta:
        verbose_name = "Картинка на слайдере"
        verbose_name_plural = "Картинки на слайдере"
        ordering = ["index"]

    def __str__(self):
        return f"{self.index}. {self.overlay_text}"


class IndexTileImage(BaseImageWithText):
    index = models.IntegerField(("Порядковый номер"))

    class Meta:
        verbose_name = "Картинка в плитке"
        verbose_name_plural = "Картинки на плитке"
        ordering = ["index"]

    def __str__(self):
        return f"{self.index}. {self.overlay_text}"
