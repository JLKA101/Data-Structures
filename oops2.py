#ticket booking record
class movieticket:
    def __init__(self, booking_id, movie_name, customer_name, seat_number, ticket_price):
        self.booking_id = booking_id
        self.movie_name = movie_name
        self.customer_name = customer_name
        self.seat_number = seat_number
        self.ticket_price = 0
        self.booking_status = "Available"
        self.set_ticket_price(ticket_price)

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, price):
        if price >= 0:
            self.ticket_price = price
        else:
            print("Ticket price cannot be negative.")

    def get_booking_status(self):
        return self.booking_status

    def set_booking_status(self, status):
        if status in ["Available", "Booked", "Cancelled"]:
            self.booking_status = status
        else:
            print("Invalid booking status.")

    def book(self, customer_name):
        if self.booking_status == "Booked":
            print("This seat is already booked.")
        else:
            self.customer_name = customer_name
            self.set_booking_status("Booked")
            print("Ticked booked successfully.")

    def cancel(self):
        if self.booking_status != "Booked":
            print("This ticket is not currently booked")
        else:
            self.set_booking_status("Cancelled")
            print("Booking cancelled")

    def display(self):
        print(f"Booking ID: {self.booking_id} | Movie: {self.movie_name} | "
              f"Seat {self.seat_number} | Customer: {self.customer_name} | "
              f"Status: {self.booking_status} | Rs {self.ticket_price:.2f}")

tickets = [
    movieticket(1, "JJK 0", "Not assigned", "A1", 5),
    movieticket(2, "JJK 0", "Not assigned", "A1", 5),
    movieticket(3, "JJK 0", "Not assigned", "A1", 5)
]

while True:
    print("")