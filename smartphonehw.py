class Smartphone:
    def __init__ (self, model, battery_lvl):
        self.model = model
        self.battery_lvl = battery_lvl

    def use_app(self):
        if self.battery_lvl > 19:
            self.battery_lvl -= 20
            print(f"Your battery level is currently {self.battery_lvl}%.")
        else:
            print("Not enough battery to use app! Please recharge.")

    def charge(self):
        self.battery_lvl = 100

    def get_battery(self):
        print(f"Your battery level is currently {self.battery_lvl}%.")

my_phone = Smartphone("Apple -1", 56)
while True:
    query = input("Would you like to use an app, charge, or check your battery percentage? ")
    if query == "Use an app":
        my_phone.use_app()
    elif query == "Check":
        my_phone.get_battery()
    elif query == "Charge":
        my_phone.charge()
        print("Phone has charged.")
    else:
        print("Invalid query. Type 'Use an app', 'Check' or 'Charge'.")