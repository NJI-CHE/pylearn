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
