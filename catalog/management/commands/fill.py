import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('category.json', encoding='UTF-8') as file:
            result = json.load(file)
            commands_list = []
            for item in result:
                commands_list.append(item)
            return commands_list

    @staticmethod
    def json_read_products():
        with open('product.json', encoding='UTF-8') as file:
            result = json.load(file)
            commands_list = []
            for item in result:
                commands_list.append(item)
            return commands_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], category_name=category['fields']['category_name'],
                         category_description=category['fields']['category_description'])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], category=Category.objects.get(pk=product['fields']['category']),
                        product_name=product['fields']['product_name'], price=product['fields']['price'],
                        description=product['fields']['description'])
            )
        Product.objects.bulk_create(product_for_create)
