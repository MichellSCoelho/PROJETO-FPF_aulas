import django_filters
from .models import Client, Product, Employee, Sale


class ClienteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cpf = django_filters.CharFilter(lookup_expr='exact')
    rg = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'cpf', 'rg']


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    registration = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['id', 'name', 'registration']


class ProductFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['description', 'quantity']


class SaleFilter(django_filters.FilterSet):
    id_client = django_filters.NumberFilter(field_name='id_client')
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr='icontains')
    id_employee = django_filters.NumberFilter(field_name='id_employee')
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='icontains')
    id_product = django_filters.NumberFilter(field_name='id_product')
    product_description = django_filters.CharFilter(field_name='product__description', lookup_expr='icontains')

    class Meta:
        model = Sale
        fields = ['id', 'id_client', 'client_name', 'id_employee', 'employee_name', 'id_product', 'product_description']