from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save

#permite comprobar si hay avatar existente y borrarlo en caso de que se cargue otro
def custom_upload_to(instance, filename):
    old_intance = Profile.objects.get(pk=instance.pk)#recupera la instancia
    old_intance.avatar.delete()#borra el avatar anterior
    return 'profiles/' + filename #devuelve el profile con el nuevo avatar


# Create your models here.
#modelo de usuarios
class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models. TextField(null=True, blank=True)
    link = models.URLField(max_length=200,null=True, blank=True)
    class Meta:
        ordering = ['user__username']

#permite asociar una instancia a un perfiles, para que no queden perfiles sin instancia 
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se creó un usuario y perfil enlazados")


