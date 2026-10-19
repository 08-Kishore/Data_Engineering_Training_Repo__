class Product:
    def __init__(self,product_id,product_name,price,stock):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.stock=stock

    def display_product(self):
        print(self.product_id)
        print(self.product_name)
        print(self.price)
        print(self.stock)

    def calculate_value(self):
        self.price=(self.price*self.stock)
        print(self.price)

obj1=Product(1,"apple",10,5)
obj2=Product(2,"banana",10,5)

class DiscountProduct(Product):
    def __init__(self, discount_percentage, product_name, price, stock, product_id):
        super().__init__(product_id, product_name, price, stock)
        self.discount_percentage=discount_percentage

    def display_product(self):
        print(self.product_id)
        print(self.product_name)
        print(self.price)
        print(self.stock)
        print(self.discount_percentage)

class PremiumProduct():
    def __init__(self,product_id, premium_percentage, product_name, price, stock):
        self.premium_percentage=premium_percentage
        self.product_name=product_name
        self.price=price
        self.stock=stock
        self.product_id=product_id

    def display_product(self):
        print(self.product_id)
        print(self.product_name)
        print(self.price)
        print(self.stock)
        print(self.premium_percentage)


product1=[
    Product(1,"apple",10,5),
    DiscountProduct(2,"banana",10,5,101),
    PremiumProduct(1,50,"apple",10,5)
]
for product in product1:
    product.display_product()