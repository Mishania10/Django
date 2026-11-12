from django.conf import settings
from django.db import models


class Request(models.Model):
    class Category(models.TextChoices):
        EQUIPMENT = 'equipment', 'Оборудование'
        SOFTWARE = 'software', 'Программное обеспечение'
        NETWORK = 'network', 'Сеть и доступ'
        OTHER = 'other', 'Другое'

    class Status(models.TextChoices):
        NEW = 'new', 'Новая'
        IN_PROGRESS = 'in_progress', 'В работе'
        WAITING = 'waiting', 'Ожидает ответа'
        CLOSED = 'closed', 'Закрыта'

    class Priority(models.TextChoices):
        LOW = 'low', 'Низкий'
        NORMAL = 'normal', 'Обычный'
        HIGH = 'high', 'Высокий'

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='support_requests',
        verbose_name='Пользователь',
    )
    name = models.CharField('Имя заявителя', max_length=150)
    email = models.EmailField('Электронная почта')
    title = models.CharField('Тема', max_length=200)
    category = models.CharField('Категория', max_length=20, choices=Category.choices, default=Category.OTHER)
    priority = models.CharField('Приоритет', max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    description = models.TextField('Описание обращения')
    status = models.CharField('Статус', max_length=20, choices=Status.choices, default=Status.NEW)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_support_requests',
        verbose_name='Исполнитель',
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'№{self.pk} — {self.title}'
