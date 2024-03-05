from django.db import models,connection
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_tenants.models import TenantMixin, DomainMixin

# from django.db import connection
class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=50, unique=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
class Domain(DomainMixin):
    pass

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(max_length=15, validators=[phone_number_regex], unique=True)

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        # Validate unique combination of email and phone number
        existing_user = User.objects.filter(email=self.email, phone_number=self.phone_number, tenant=self.tenant).first()
        if existing_user and existing_user.id != self.id:
            raise ValueError("A user with this email and phone number already exists.")
        
        super().save(*args, **kwargs)

# Create your models here.
