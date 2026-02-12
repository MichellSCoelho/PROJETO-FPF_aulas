from rest_framework import serializers

from .models import Client, Product, Employee, Sale

class ClienteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    age = serializers.IntegerField(
        min_value=18, max_value=100
    )


    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'description', 'quantity']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'registration']


class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),source='product', write_only=True)
    client = ClienteSerializer(read_only=True)
    id_client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), source='client', write_only=True)
    employee = EmployeeSerializer(read_only=True)
    id_employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)


    class Meta:
        model = Sale
        fields = ['id','product_id','product','id_client','client','employee_id','employee','nrf']
