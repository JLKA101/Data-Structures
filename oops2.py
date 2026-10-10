#ticket booking record
class movieticket:
    def __init__ (self, movie, name, seat, price, status):
        self.movie = movie
        self.name = name
        self.seat = seat
        self.price = 0
        self.status = "Available" #booking/ticket
        self.set_price(price)

    def get_price(self):
        return self.price

    def set_price(self, newPrice):
        if newPrice >= 0:
            self.price = newPrice
        else:
            print("Ticket price must not be negative.")

    def book(self, price, movie, name, seat, status):
        movie = input("What movie would you like to see?")
        name = input("What is your name?")
        seat = input("Where would you like to sit?")

        if seat 
        ticket1 = movieticket(f"{name} will be seeing {movie} in seat {seat}.")



    