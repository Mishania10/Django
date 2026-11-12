from django.apps import AppConfig


class CatalogConfig(AppConfig):
    class AccountsConfig(AppConfig):
        default_auto_field = 'django.db.model.BigAutoField'
        name = 'apps.catalog'
        verbose_name = 'Пользователи'
