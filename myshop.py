from datetime import datetime
from time import sleep
import os

from pony.orm import (
    Database,
    Required, Optional, Set, PrimaryKey,
    LongStr,
    set_sql_debug, show, db_session, select
)


db = Database('sqlite', 'estore.sqlite', create_db=True)


class Category(db.Entity):
    """Категория товара"""
    title = Required(str, 50)
    description = Optional(LongStr)
    parent = Optional('Category', reverse='categories')
    media = Set('Media')
    products = Set('Product')
    categories = Set('Category', reverse='parent')


class Product(db.Entity):
    """Товар"""
    title = Required(str, 255)
    price = Required(float)
    description = Optional(LongStr)
    categories = Set(Category)
    comments = Set('Comment')
    media = Set('Media')
    order_items = Set('OrderItem')
    cart_items = Set('CartItem')

class Customer(db.Entity):
    """Покупатель"""
    phone = Required(str, 20, unique=True)
    email = Optional(str, 100)
    name = Optional(str, 255)
    discount = Optional(float, default=1) # размер скидки
    orders = Set('Order')
    cart = Optional('Cart')

class Order(db.Entity):
    """Заказ"""
    customer = Required(Customer)
    status = Required('Status')
    created = Optional(datetime, default=datetime.now)
    # created = Optional(datetime)
    order_items = Set('OrderItem')

    # def before_insert(self):
    #     super().before_insert()
    #     self.created = datetime.now()

class Status(db.Entity):
    """Справочник статус"""
    name = PrimaryKey(str, 50)
    orders = Set('Order')

class OrderItem(db.Entity):
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    order = Required(Order)

class Cart(db.Entity):
    """Корзина"""
    customer = Optional(Customer, nullable=True)
    cart_items = Set('CartItem')

class CartItem(db.Entity):
    """Продукт в корзине"""
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    cart = Required('Cart')

class Media(db.Entity):
    """Мультимедиа ресурс"""
    categories = Set('Category')
    products = Set('Product')

class Comment(db.Entity):
    """Комментарии"""
    product = Required('Product')


# class Sale(object):
#     """Размер скидок, промокод"""


set_sql_debug(True)
db.generate_mapping(create_tables=True)


with db_session:
    customer1 = Customer(name='Rob', phone='+321112315')
    customer2 = Customer(name='Bob', phone='+3261123114')
    customer3 = Customer(name='Peter', phone='+321611113')
    customer = Customer[1]
    show(customer)


@db_session
def show_table(table):
    show(select(querry for querry in table ))

#show_table(Customer)
