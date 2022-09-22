from django.contrib.auth.models import User
from product.models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

# User modelinde save işlemi yapıldığında
# işlem başladıktan hemen sonra  aşağıdaki işlemi çalıştırır
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs ):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()


