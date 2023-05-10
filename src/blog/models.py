from pprint import pprint

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #     , on_delete=models.SET_DEFAULT, default=1)   avec par exemple le nom de l'autheur du key1 = "Hautheur inconnu"
    #     , on_delete=models.SET_NULL, null=True) On casse le lien de l'article avec son hateur
    #     , on_delete=PROTECT) protege l'article => erreur = l'hauteur ne peut être détruit car un article lui est associé
    category = models.ManyToManyField(Category)



