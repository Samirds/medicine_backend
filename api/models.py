from django.db import models
from users.models import CustomUser


# --------------------------------------- API Model -------------------------------------------------------------
# class Advertisable(models.Model):
#     is_adv = models.BooleanField(default=False)
#     def __bool__(self):
#          return self.is_adv



class Brand_Type(models.Model):
    name = models.CharField(max_length=50,)
    image = models.ImageField(upload_to="Images", max_length=250, null=True, blank=True)
    def __str__(self):
         return self.name




class Brand(models.Model):
    name = models.CharField(max_length=50,)
    image = models.ImageField(upload_to="Images", max_length=250, null=True, blank=True)
    def __str__(self):
         return self.name


# class Corona_Prod(models.Model):
#     is_corona_prod = models.BooleanField(default=False)
#     def __str__(self):
#          return self.is_corona_prod


class Compositions(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
         return self.name


class Prod_Age_Cat(models.Model):
    cat = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Images", max_length=250, null=True, blank=True)
    def __str__(self):
         return self.cat

class Prod_Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
         return self.type


class Prod_Usage_Cat(models.Model):
     usage_cat = models.CharField(max_length=50, blank=True, null=True)
     image = models.ImageField(upload_to="Images", max_length=250, null=True, blank=True)
     def __str__(self):
          return self.usage_cat


# from users.models import CustomUser

class Product_Information(models.Model):
    is_adv = models.BooleanField(default=False)
    availability = models.IntegerField(null=True)
    name = models.CharField(max_length=50) 
    exp_date = models.DateTimeField()
    price = models.IntegerField()
    Strip_contain = models.IntegerField(null=True, blank=True)
    usage = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    info = models.TextField(max_length=500, null=True, blank=True)
    is_corona_prod = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Images", max_length=250, null=True, blank=True)
    

    
    # login = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #advertisable = models.ForeignKey(Advertisable, on_delete=models.SET_DEFAULT, default=False, related_name="adv_related")
    brand_type = models.ForeignKey(Brand_Type, on_delete=models.SET_NULL, null=True, related_name="brand_typr_related")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="brand_related")
    #corona_prod = models.ForeignKey(Corona_Prod, on_delete=models.SET_DEFAULT, default=False, related_name="corona_related")
    prod_age_cat = models.ManyToManyField(Prod_Age_Cat, related_name="prod_age_related")
    prod_type = models.ForeignKey(Prod_Type, on_delete=models.SET_NULL, null=True, related_name="prod_type_related")
    compositions = models.ManyToManyField(Compositions, related_name="comp_related")
    prod_usage_cat = models.ForeignKey(Prod_Usage_Cat, on_delete=models.SET_NULL, null=True, verbose_name="Usage Category")


    def __str__(self):
         return self.name

