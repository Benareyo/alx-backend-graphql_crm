import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphql_crm.settings")
django.setup()


from crm.models import Customer, Product

# Seed customers
customers = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Carol", "email": "carol@example.com"},
]

for c in customers:
    Customer.objects.get_or_create(**c)

# Seed products
products = [
    {"name": "Laptop", "price": 999.99, "stock": 10},
    {"name": "Mouse", "price": 25.50, "stock": 100},
]

for p in products:
    Product.objects.get_or_create(**p)

print("Database seeded successfully!")

