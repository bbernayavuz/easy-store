from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

# product, signals'ın içnde de import edildiği için
# en üstten import etmek yerine ready kullanılıyor.

    def ready(self):
        import api.signals