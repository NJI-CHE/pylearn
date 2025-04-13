## Reataurant class qui a un Menu, Table reservation er management of orders
#Atrributes: menuItems, book_table, customer_order, and methods like add_item_to_menu,
#book_tables and customer_orer

###Perform the follwing task
# Add items to menu
# Make table reservations
#Take customer orders
#Print Menu
#Print table reservations
#Print Customer orders
# ####

class Restaurant:
    def __init__(self):
        self.menu_items= {}
        self.book_table = []
        self.customer_orders = []
    
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order':order}
        self.customer_orders.append(order_details)

    #Define print functions for displaying all the data
    
    def print_menu_item(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))

    def print_table_reservation(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_order(self):
        for order in self.customer_orders:
            print("Tables {}:{}".format(order['table_number'], order['order']))

restaurant = Restaurant()


#Add items
restaurant.add_item_to_menu("cheeseburger", 9.99)
restaurant.add_item_to_menu('Salad', 8)
restaurant.add_item_to_menu('Grilled Salmon', 19.99)
restaurant.add_item_to_menu('French fries', 3.99)
restaurant.add_item_to_menu('Couscous:', 15)

#Book tables
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

#Order items
restaurant.customer_order(1, "cheeseburger")
restaurant.customer_order(1, "Couscous")
restaurant.customer_order(2, "Fish & chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_item()

print("\nTable reserved in the restaurant:")
restaurant.print_table_reservation()

print("\nPrint Customer orders:")
restaurant.print_customer_order()

