import time
name = input("Please enter your name: ")
# ---------Obersever----------------
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{}{}, bon Appetit!'.format(message, self.name))
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

client = Subscriber(name)
pub = Publisher()
# ---------Obersever----------------


#
class Singleton:
    def __init__(self, ordermessage):
        self.ordermessage = ordermessage

#

class Order:
  '''Subsystem # 1'''
  
  def takeorder(self):
    singleton = Singleton("Processing your order...")
    print(singleton.ordermessage)


class Cooking:
  '''Subsystem # 2'''

  def cook(self):
    singleton = Singleton("Cooking...")
    print(singleton.ordermessage)


class Bringing:
  '''Subsystem # 3'''

  def bring(self):
    pub.register(client)
    pub.dispatch("Your order is ready, ")


class MakingFastFood1:
  '''Facade'''

  def __init__(self):
    self.Order = Order()


  def startOrder(self):
    self.Order.takeorder()


class MakingFastFood2:
  '''Facade'''

  def __init__(self):
    self.Cooking = Cooking()

  def startOrder(self):
    self.Cooking.cook()



class MakingFastFood3:
  '''Facade'''

  def __init__(self):

    self.Bringing = Bringing()

  def startOrder(self):

    self.Bringing.bring()




# Burger_Object Interface
class Burger(object):
    def cook(self):
        pass


# Subclasses of  Burger
class BeefBurgers(Burger):
    def cook(self):
        print(b_quantity,"x",'Beef Burgers')
class ChickenBurger(Burger):
    def cook(self):
        print(b_quantity,"x",'Chicken Burger')

class FishBurger(Burger):
    def cook(self):
        print(b_quantity,"x",'Fish Burger')
class CheeseBurger(Burger):
    def cook(self):
        print(b_quantity,"x","Cheese Burger")


# Soda_Object Interface
class Soda(object):
    def bring(self):
        pass

# Subclasses of Soda
class Sprite(Soda):
    def bring(self):
        print(s_quantity,"x","Sprite")
class Fanta(Soda):
    def bring(self):
        print(s_quantity,"x","Fanta")
class Cola(Soda):
    def bring(self):
        print(s_quantity,"x","Cola")
class Pepsi(Soda):
    def bring(self):
        print(s_quantity,"x","Pepsi")


# Pizza_Object Interface
class Pizza(object):
    def bring(self):
        pass

# Subclasses of Pizza
class Margarita(Pizza):
    def bring(self):
        print(p_quantity,"x","Margarita")
class Neapolitan(Pizza):
    def bring(self):
        print(p_quantity,"x","Neapolitan")
class New_York_Style(Pizza):
    def bring(self):
        print(p_quantity,"x","New York-Style")
class Chicago(Pizza):
    def bring(self):
        print(p_quantity,"x","Chicago")
class Sicilian(Pizza):
    def bring(self):
        print(p_quantity,"x","Sicilian")


# Burger_Factory Object
class BurgerStoreFactory(object):
    @staticmethod
    def getBurger(name):
        if name == 'Beef':
            return BeefBurgers()
        elif name == 'Chicken':
            return ChickenBurger()
        elif name == 'Fish':
            return FishBurger()
        elif name == 'Cheese':
            return CheeseBurger()


# Soda_Factory Object
class SodaStoreFactory(object):
    @staticmethod
    def getSoda(name):
        if name == 'Cola':
            return Cola()
        elif name == 'Pepsi':
            return Pepsi()
        elif name == 'Sprite':
            return Sprite()
        elif name == 'Fanta':
            return Fanta()
#Pizza_Factory Object
class PizzaStoreFactory(object):
    @staticmethod
    def getPizza(name):
        if name == 'Sicilian':
            return Sicilian()
        elif name == 'Chicago':
            return Chicago()
        elif name == 'New York-Style':
            return New_York_Style()
        elif name == 'Neapolitan':
            return Neapolitan()
        elif name == 'Margarita':
            return Margarita()

# Price Counting

class Quantity():
    def count_quantity(self):
        if b_quantity != 0:
            b_price = b_quantity * 1600
        if s_quantity != 0:
            s_price = s_quantity * 400
        if p_quantity != 0:
            p_price = p_quantity * 2500
        if b_quantity == 0:
            b_price = 0
        if s_quantity == 0:
            s_price = 0
        if p_quantity == 0:
            p_price = 0
        total_price =  b_price + s_price + p_price
        return total_price

class Menu():
    def burger_menu(self):
        print("Burger Menu:")
        print(" 1- Beef Burger\n 2 - Chicken Burger\n 3 - Cheese Burger\n 4 - Fish Burger \n 0 - None")

    def soda_menu(self):
        print("Soda Menu: ")
        print(" 1 - Cola\n 2 - Sprite \n 3 - Fanta \n 4 - Pepsi \n 0 - None")
    def pizza_menu(self):
        print("Pizza Menu: ")
        print(" 1 - Margarita\n 2 - Neapolitan \n 3 - New York-Style \n 4 - Chicago \n 5 - Sicilian \n 0 - None ")
        
# Client Code
if __name__ == '__main__':
    makingfastfood1 = MakingFastFood1()
    makingfastfood1.startOrder()


    m = Menu()
    m.burger_menu()
    b_no = int(input("Choose Burger:"))
    while b_no in range(5,99):
        m.burger_menu()
        b_no = int(input("Choose Burger:"))
        b_quantity = int(input("Enter quantity of Burger: "))
    if b_no != 0:
        b_quantity = int(input("Enter quantity of Burger: "))

    m.soda_menu()
    s_no = int(input("Choose Soda: "))
    while s_no is False:
        m.soda_menu()
        s_no = int(input("Choose Soda: "))
        s_quantity = int(input("Enter quantity of Soda: "))
    if s_no != 0:
        s_quantity = int(input("Enter quantity of Soda: "))


    m.pizza_menu()
    p_no = int(input("Choose Pizza: "))
    while p_no is  False:
        m.pizza_menu()
        p_no = int(input("Choose Pizza: "))
        p_quantity = int(input("Enter quantity of Pizza: "))
    if p_no != 0:
        p_quantity = int(input("Enter quantity of Pizza: "))
    print("You ordered: ")
    b = BurgerStoreFactory()
    if b_no== 1:
        burger = b.getBurger('Beef')
        burger.cook()
    elif b_no== 2:
    # Create burger "Chicken burger"
        burger = b.getBurger('Chicken')
        burger.cook()
    elif b_no== 4:
    # Create burger "Fish burger"
        burger = b.getBurger('Fish')
        burger.cook()
    elif b_no== 3:
        burger = b.getBurger('Cheese')
        burger.cook()
    elif b_no == 0:
        print()
        b_quantity = 0
    s = SodaStoreFactory()
    if s_no == 3:
        soda = s.getSoda('Fanta')
        soda.bring()
    elif s_no == 1:
        soda = s.getSoda('Cola')
        soda.bring()
    elif s_no == 2:
        soda = s.getSoda('Sprite')
        soda.bring()
    elif s_no == 4:
        soda = s.getSoda('Pepsi')
        soda.bring()
    elif s_no == 0:
        s_quantity = 0
    p = PizzaStoreFactory()
    if p_no == 2:
        pizza = p.getPizza('Neapolitan')
        pizza.bring()
    elif p_no == 3:
        pizza = p.getPizza('New York-Style')
        pizza.bring()
    elif p_no == 4:
        pizza = p.getPizza('Chicago')
        pizza.bring()
    elif p_no == 5:
        pizza = p.getPizza('Sicilian')
        pizza.bring()
    elif p_no == 1:
        pizza = p.getPizza('Margarita')
        pizza.bring()
    elif p_no == 0:
        p_quantity = 0

    quan = Quantity()
    print("Total Price: ", quan.count_quantity())


    time.sleep(5)
    makingfastfood2 = MakingFastFood2()
    makingfastfood2.startOrder()

    time.sleep(5)
    makingfastfood3 = MakingFastFood3()
    makingfastfood3.startOrder()



