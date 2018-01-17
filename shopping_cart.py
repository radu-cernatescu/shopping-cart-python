#Cart class is defined
class Cart(object):
    #__init__ method is defined
    def __init__(self,customer):
        #self.customer is defined using the user defined input
        self.customer = customer
        #if the customer country is Canada, a tax of 13 percent is added to the price along with free shipping
        if customer.country == "canada":
            self.tax = 0.13
            self.shipping = 0
        #if the customer country is not Canada, not tax is applied and a fee of $30 for shipping is added
        else:
            self.tax = 0
            self.shipping = 30

        #an empty list used to hold all of the products is initialized
        self.item_list = []
    #the add_item method is defined which adds a product to the cart of the customer
    def add_item(self,product,quantity):
        #appends the product to the item list
        self.item_list.append(Cart_Item(product,quantity))
    #the print_item_list method is defined which prints the list of all products in the item list in a chart format
    def print_item_list(self):
        print "{:<10}{:^25}{:<20}".format("Product Name","Unit price","Quantity")
        print "-"*50
        for i in self.item_list:
            print "{:<10}{:^25}{:>7}".format(i.product.name,("$"+str(i.product.unit_price)),i.quantity)
    #the check out method is defined which uses the print item list and compiles the total cost
    def check_out(self):
        print "Hello,",self.customer.first_name,self.customer.last_name+". You are shopping from", self.customer.country.capitalize()+".\n"
        print "This is your cart:\n"
        self.print_item_list()
        sub_total =0
        for item in self.item_list:
            sub_total+= item.get_Cost()
        print " "
        print "Subtotal: $",round(sub_total,2)
        print "Tax:",self.tax*100,"%"
        print "Shipping: $",self.shipping
        print "Total: $",round(+sub_total+sub_total*self.tax+self.shipping,2)

#Cart_Item class is defined
class Cart_Item(object):
    #the __init__ method is defined
    def __init__(self,product,quantity):
        #the product and quantity variables are defined based on input
        self.product = product
        self.quantity = quantity
    #the get_cost method is defined
    def get_Cost(self):
        #returns the total
        return self.product.unit_price*self.quantity

#Product class is defined
class Product(object):
    #__init__ method is defined
    def __init__(self,name,unit_price):
        #the name and unit price of the product is defined based on the input
        self.name = name
        self.unit_price = unit_price

#Person class is defined
class Person(object):
    #__init__ method is defined
    def __init__(self,first_name,last_name,country):
        #first name, last name, and country is defined based on the input
        self.first_name = first_name
        self.last_name = last_name
        self.country = country

#main function is defined
def main():
    #The user is asked to input their first name, last name and country
    first_name = raw_input("Enter your first name")
    last_name = raw_input("Enter your last name")
    country = raw_input("Enter your country").lower()
    #the customer1 instance is defined
    customer1 = Person(first_name,last_name,country)
    #the my_cart instance is defined
    my_cart = Cart(customer1)
    #five instances of products are defined
    product1 = Product("Banana",2.99)
    product2 = Product("Apple",3.99)
    product3 = Product("Beef",29.99)
    product4 = Product("Papaya",4.99)
    product5 = Product("Mango",5.99)
    #the five products are added to cart
    my_cart.add_item(product1,5)
    my_cart.add_item(product2,6)
    my_cart.add_item(product3,2)
    my_cart.add_item(product4,16)
    my_cart.add_item(product5,4)
    #the check out method is called for my_cart
    my_cart.check_out()

#main function is called
main()