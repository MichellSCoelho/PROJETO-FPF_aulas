from django.db import models

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    class Meta:
        abstract = True
        managed = True


class Product(ModelBase):
    description = models.TextField(
        db_column='tx_description',
        null=False
    )
    quantity = models.IntegerField(
        db_column='int_quantity',
        null=False,
        default=0
    )
    def __str__ (self):
        return f"{self.description [:30]}... - Qtd:{self.quantity}"


class Client(ModelBase):
    name = models.CharField(
        max_length=70,
        db_column='tx_name',
        null=False,
        blank=False
    )
    age = models.IntegerField(
        db_column='int_age',
        null=False
    )
    rg = models.CharField(
        max_length=12,
        db_column='tx_rg',
        null=False,
        unique=True,
        blank=False
    )
    cpf = models.CharField(
        max_length=12,
        db_column='tx_cpf',
        null=False,
        unique=True,
        blank=False
    )
    def __str__(self):
        return f"{self.id} - {self.name}"

class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=70
    )
    registration = models.CharField(
        db_column='tx_registration',
        null=False,
        max_length=15,
        unique=True,
        blank=False
    )

class Sale(ModelBase):
    product = models.ForeignKey(
        Product,
        db_column='id_product',
        null=False,
        on_delete=models.DO_NOTHING
    )
    client = models.ForeignKey(
        Client,
        db_column='id_client',
        null=False,
        on_delete=models.DO_NOTHING
    )
    employee = models.ForeignKey(
        Employee,
        db_column='id_employee',
        null=False,
        on_delete=models.DO_NOTHING
    )
    nrf = models.CharField(
        db_column='tx_nrf',
        max_length=10,
        null=False
    )