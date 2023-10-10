from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, age, gender, last_name=None, address=None, pincode=None, **extra_fields):
         if not email:
            raise ValueError(" Email is Required for the Registration.")
         
         if not first_name:
            raise ValueError(" First Name is Required for the Registration.")
         
         if not age:
            raise ValueError(" Age is Required for the Registration.")
         
         if not gender:
            raise ValueError(" Gender is Required for the Registration.")
         
         email = self.normalize_email(email)
         first_name = self.normalize_email(first_name)

         user = self.model(email=email, first_name=first_name, age=age, gender=gender, last_name=last_name, address=address, pincode=pincode, **extra_fields)
         user.set_password(password)
         user.save()
         return user
    

    def create_superuser(self, email, password, first_name, age, gender, last_name=None, address=None, pincode=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, first_name, age, gender, **extra_fields)