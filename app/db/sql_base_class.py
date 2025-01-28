from .sql_base import SqlBase, engine
from ..models.customer import Customer
from ..models.user import User
from ..models.product import Product
from ..models.orders import Order
from ..models.order_items import OrderItem

SqlBase.metadata.create_all(engine)
