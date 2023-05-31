from django.db import models
from django.utils.translation import gettext as _
import uuid
from users.models import User


class Publisher(models.Model):
    name = models.CharField(_("Publisher"), max_length=50)

    def __str__(self):
        return self.name
    
    @property
    def id(self):
        return self.id
    

class Book(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False, unique=True)
    owner = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=50)
    authors = models.ManyToManyField(User, verbose_name=_("Authors"),related_name='authors')
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, verbose_name=_("Publisher"), on_delete=models.CASCADE)
    pubdate = models.DateField(_("date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
    

class Store(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    books = models.ManyToManyField("Book", verbose_name=_("books"))

    def __str__(self):
        return self.name