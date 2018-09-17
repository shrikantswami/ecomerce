from django.db import models
import random
import os

def get_filename_ext(filename):
    base_name=os.path.basename(filename)
    name , ext =os.path.splitext(base_name)
    return name,ext

def uplod_image_path(instance,filename):
    random_name=random.randint(1,2135132135)
    name, ext=get_filename_ext(filename)
    random_name=str(random_name)
    list=["products_image/",random_name,ext]
    new_filename="".join(list)
    return str(new_filename)

class ProductsQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(bookmarked=True)


class ProductsManager(models.Manager):
    def get_by_id(self, id):
        qs=self.get_queryset().filter(id=id)
        if qs.count() == 1 :
            return qs.first()
        return None  #Products.objects == get_queryset
    def featured(self):
        #return self.get_queryset().filter(bookmarked=True)
        return ProductsQuerySet(self.model,using=self._db)

    def get_queryset(self):
        #return self.get_queryset().filter(bookmarked=True)
        return ProductsQuerySet(self.model,using=self._db)
# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    # image=models.ImageField(upload_to="products_image",null=True)
    image=models.ImageField(upload_to=uplod_image_path,null=True)
    bookmarked =models.BooleanField(default=False)

    objects=ProductsManager()
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("product_detail",kwargs={'pk':self.pk})
