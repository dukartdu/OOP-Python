
import csv


class Item:
    pay_rate = 0.8 #pay rate after 20 % discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
       #run validations to received arguments
       assert price >= 0, f"Price {price} si not greater than zero !"
       assert quantity >= 0, f"Quantity {quantity} is not greater tham zero !"

       #assign to self object
       self.__name = name
       self.__price = price
       self.quantity = quantity

       #actions to execute
       Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    #orioerty decorator = read only attribute or getter
    def name(self):
        return self.__name

    @name.setter
    #setter
    def name(self, value):
        if len(value) > 10:
            raise Exception ("The name is tool long!")
        else:
            self.__name = value




    def calculate_total_price(self):
        return self.price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        hello someone,
        we have {self.name} {self.quantity} times.
        Regards, Juozapas
        """
    
    def __send(self):
        pass

        # impossible to acces connect, prepare_body and send from main file only can acccess send_email 
        #good if you want to hide functions and info
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()