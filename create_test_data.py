import os
import django

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Product, Attr, ProductAttr, UniqueProduct


def create_test_data():
    # Создание экземпляров моделей
    product1 = Product.objects.create(name="Product 1")
    product2 = Product.objects.create(name="Product 2")
    product3 = Product.objects.create(name="Product 3")

    attr1 = Attr.objects.create(name="Attr 1")
    attr2 = Attr.objects.create(name="Attr 2")
    attr3 = Attr.objects.create(name="Attr 3")

    product_attr1 = ProductAttr.objects.create(product=product1, attr=attr1, value="Value 1")
    product_attr2 = ProductAttr.objects.create(product=product2, attr=attr2, value="Value 2")
    product_attr3 = ProductAttr.objects.create(product=product3, attr=attr3, value="Value 3")
    product_attr4 = ProductAttr.objects.create(product=product1, attr=attr2, value="Value 4")
    product_attr5 = ProductAttr.objects.create(product=product2, attr=attr3, value="Value 5")

    # Создание уникальных продуктов
    unique_product1 = product1.unique_products.generate(attr=product_attr1)
    unique_product2 = product2.unique_products.generate(attr=product_attr2)
    unique_product3 = product3.unique_products.generate(attr=product_attr3)
    unique_product4 = product1.unique_products.generate(attr=product_attr4)
    unique_product5 = product2.unique_products.generate(attr=product_attr5)

    # Вывод информации о созданных уникальных продуктах
    unique_products = [unique_product1, unique_product2, unique_product3, unique_product4, unique_product5]
    for up in unique_products:
        print(f"Unique Product ID: {up.id}")
        print(f"  Product name: {up.product.name}")
        print(f"  Product attribute value: {up.attr.value}")
        print(f"  Product attribute name: {up.attr.attr.name}")


if __name__ == '__main__':
    create_test_data()
