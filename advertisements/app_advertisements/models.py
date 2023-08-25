from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from .validators import validate_question_mark

User = get_user_model()

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128, validators=[validate_question_mark])
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Уместен торг или нет")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisements/")

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style ="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description="Дата изменения")
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style ="color: yellow; font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description="Изображение")
    def image_picture(self):
        from django.utils.html import format_html
        from django.conf import settings
        return format_html("<img src='{}' style='max-width: 150px; max-height: 150px'/>", f"{settings.MEDIA_URL}{self.image}" if self.image != '' else '')