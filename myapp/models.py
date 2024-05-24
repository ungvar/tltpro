from django.db import models

class Attr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    attrs = models.ManyToManyField("Attr", through="ProductAttr")

    def __str__(self):
        return self.name

class ProductAttr(models.Model):
    attr = models.ForeignKey("Attr", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

class UniqueProductManager(models.Manager):
    def all(self):
        return super().all()

    def generate(self, product, attr):
        unique_product = self.create(product=product, attr=attr)
        return unique_product

class CustomForeignKey(models.ForeignKey):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.related_accessor_class = CustomReverseManyToOneManager

class CustomReverseManyToOneManager(models.Manager):
    def __init__(self, related):
        super().__init__()
        self.related = related

    def all(self):
        return UniqueProduct.objects.filter(product=self.related)

    def generate(self, attr):
        return UniqueProduct.objects.create(product=self.related, attr=attr)

class UniqueProduct(models.Model):
    product = CustomForeignKey(Product, on_delete=models.PROTECT)
    attr = models.ForeignKey(ProductAttr, on_delete=models.PROTECT)

# Добавление свойства к модели Product
Product.add_to_class('unique_products', property(lambda self: CustomReverseManyToOneManager(self)))
