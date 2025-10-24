# D-Mart Shopping bill

# Welcome message
print("     D-Mart     \n"
      "-----------------\n"
      "welcome to Dmart\n"
      "-----------------\n")

# Global variables (used as per the original structure)
qty = 0
rate = 0

class Dmart():
    """
    A class representing a simple D-Mart shopping experience with 
    methods for different product categories.
    """

    def Grocery(self):
        """Handles grocery item selection and calculation."""
        global qty, rate
        
        print("1.1)jeera\n1.2)peanuts\n1.3)wheatflour")
        item = input("choose item: ")
        # Adding error handling for non-numeric input for robustness
        try:
            n = float(input("how many kgs:"))
        except ValueError:
            print("Invalid quantity entered.")
            return

        particulars = ""
        rate = 0
        qty = 0

        if item == '1.1':
            rate = 80
            qty = qty + n
            particulars = 'jeera'
        elif item == '1.2':
            rate = 200
            qty = qty + n
            particulars = 'peanuts'
        elif item == '1.3':
            rate = 60
            qty = qty + n
            particulars = 'wheatflour'
        else:
            print("Invalid item selection")
            return
        
        value = qty * rate
        print("Id\tParticulars\tqty\trate\tvalue\n", 
              item, "\t", particulars, " \t", qty, "\t", rate, "\t", value)

    def snacks(self):
        """Handles snacks item selection and calculation."""
        global qty, rate

        print("2.1)maggie\n2.2)lays\n2.3)pasta")
        item = input("choose item: ")
        try:
            n = float(input("no.of packets:"))
        except ValueError:
            print("Invalid quantity entered.")
            return
            
        particulars = ""
        rate = 0
        qty = 0

        if item == '2.1':
            rate = 25
            qty = qty + n
            particulars = 'maggie'
        elif item == '2.2':
            rate = 10
            qty = qty + n
            particulars = 'lays'
        elif item == '2.3':
            rate = 40
            qty = qty + n
            particulars = 'pasta'
        else:
            print("Invalid item selection")
            return
        
        value = qty * rate
        print("Id\tParticulars\tqty\trate\tvalue\n", 
              item, "\t", particulars, " \t", qty, "\t", rate, "\t", value)

    def drinks(self):
        """Handles drinks item selection and calculation."""
        global qty, rate
        
        print("3.1)limca\n3.2)maza\n3.3)pepsi")
        item = input("choose item: ")
        try:
            n = float(input("no.of bottles:"))
        except ValueError:
            print("Invalid quantity entered.")
            return

        particulars = ""
        rate = 0
        qty = 0

        if item == '3.1':
            rate = 20
            qty = qty + n
            particulars = 'limca'
        elif item == '3.2':
            rate = 20
            qty = qty + n
            particulars = 'maza'
        elif item == '3.3':
            rate = 20
            qty = qty + n
            particulars = 'pepsi'
        else:
            print("Invalid item selection")
            return
        
        value = qty * rate
        print("Id\tParticulars\tqty\trate\tvalue\n", 
              item, "\t", particulars, " \t", qty, "\t", rate, "\t", value)

    def cosmetics(self):
        """Handles cosmetics item selection and calculation."""
        global qty, rate
        
        print("4.1)facewash\n4.2)cream\n4.3)moisturizer")
        item = input("choose item: ")
        try:
            n = float(input("no.of items:"))
        except ValueError:
            print("Invalid quantity entered.")
            return

        particulars = ""
        rate = 0
        qty = 0

        if item == '4.1':
            rate = 100
            qty = qty + n
            particulars = 'facewash'
        elif item == '4.2':
            rate = 10
            qty = qty + n
            particulars = 'cream'
        elif item == '4.3':
            rate = 40
            qty = qty + n
            particulars = 'moisturizer'
        else:
            print("Invalid item selection")
            return
        
        value = qty * rate
        print("Id\tParticulars\tqty\trate\tvalue\n", 
              item, "\t", particulars, " \t", qty, "\t", rate, "\t", value)

    def stationary(self):
        """
        Handles stationary item selection and calculation.
        NOTE: 'particulars' have been corrected here to match the menu item names.
        """
        global qty, rate
        
        print("5.1)box\n5.2)pen\n5.3)pencil")
        item = input("choose item: ")
        try:
            n = float(input("no.of items:"))
        except ValueError:
            print("Invalid quantity entered.")
            return

        particulars = ""
        rate = 0
        qty = 0

        if item == '5.1':
            rate = 150
            qty = qty + n
            # Corrected: Was 'pen' in the original snippet.
            particulars = 'box' 
        elif item == '5.2':
            rate = 10
            qty = qty + n
            # Corrected: Was 'pencil' in the original snippet.
            particulars = 'pen' 
        elif item == '5.3':
            rate = 5
            qty = qty + n
            # Corrected: Was 'moisturizer' in the original snippet.
            particulars = 'pencil' 
        else:
            print("Invalid item selection")
            return
        
        value = qty * rate
        print("Id\tParticulars\tqty\trate\tvalue\n", 
              item, "\t", particulars, " \t", qty, "\t", rate, "\t", value)

# --- Main Program Loop ---

# Create an instance of the Dmart class
obj = Dmart()

# Start the interactive shopping loop
while(1):
    print("\nAvailable items are:")
    print("1.grocery\n2.snacks\n3.drinks\n4.cosmetics\n5.stationary")
    user = input("select among 5 items (0 to exit): ")

    if user == '0':
        print("thank you for shopping")
        break
    elif user == '1':
        obj.Grocery()
    elif user == '2':
        obj.snacks()
    elif user == '3':
        obj.drinks()
    elif user == '4':
        obj.cosmetics()
    elif user == '5':
        obj.stationary()
    else:

        print("Invalid category selection")
