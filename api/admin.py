from django.contrib import admin
from . models import Brand, Compositions, Prod_Age_Cat, Prod_Type, Prod_Usage_Cat, Product_Information, Brand_Type
from users.models import CustomUser
# Register your models here.





# --------------------------------- Custome User -----------------------

@admin.register(CustomUser)
class userAdmin(admin.ModelAdmin):
    list_display = [ "first_name", "last_name", "email", "gender", "age", "pincode"]


# ---------------------------------------- Advertisable ----------------------------

# @admin.register(Advertisable)
# class adv_Admin(admin.ModelAdmin):
#     list_display = ["id",  "is_adv"]




# --------------------------- Brand Type--------------------------------
@admin.register(Brand_Type)
class brand_type_Admin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]



# --------------------------- Brand --------------------------------
@admin.register(Brand)
class brand_Admin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]



# ----------------------------------------------- Corona ----------------------------------
# @admin.register(Corona_Prod)
# class coro_Admin(admin.ModelAdmin):
#     list_display = ["id","is_corona_prod"]
   


# ------------------------------------ composiotin --------------------------

@admin.register(Compositions)
class comp_Admin(admin.ModelAdmin):
    list_display = ["id", "name"]


# --------------------------------- Prod_Age -----------------------------

@admin.register(Prod_Age_Cat)
class prod_age_Admin(admin.ModelAdmin):
    list_display = ["id", "cat", "image"]


# ----------------------------------------------------- Prod Type -----------------------
@admin.register(Prod_Type)
class prod_typ_Admin(admin.ModelAdmin):
    list_display = ["id", "type"]


    

# --------------------------- Prod Usage Category --------------------------------
@admin.register(Prod_Usage_Cat)
class prod_usage_cat_Admin(admin.ModelAdmin):
    list_display = ["id", "usage_cat", "image"]


# --------------------------------- Prod Information -----------------------------------

@admin.register(Product_Information)
class prod_inf_Admin(admin.ModelAdmin):
    list_display = ["id", "name", "exp_date", "price", "image", "brand_type","brand", "prod_usage_cat"]