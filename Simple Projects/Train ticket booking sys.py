from random import randint
import time

class Train:
    def __init__(self, trainno, fro, to, class_type): #constructor 
        self.trainno = trainno
        self.fro = fro
        self.to = to
        self.class_type = class_type
        self.fare = randint(100, 500)
        self.bookings = []

    def book_ticket(self, passenger_name):
        ticket_id = f"TKT{randint(1000,9999)}"
        booking = {
            "ticket_id": ticket_id,
            "passenger": passenger_name,
            "from": self.fro,
            "to": self.to,
            "class": self.class_type,
            "fare": self.fare,
            "status": "Confirmed"
        }
        self.bookings.append(booking)
        print(f"\nTicket booked successfully for {passenger_name}")
        print(f"Ticket ID: {ticket_id}")
        print(f"Train No.: {self.trainno}, Route: {self.fro} to {self.to}")
        print(f"Class: {self.class_type}, Fare: ${self.fare}")
        print(f"Status: Confirmed\n")

    def view_bookings(self):
        if not self.bookings:
            print("\nNo bookings made yet.\n")
            return
        print("\nAll Bookings:\n")
        for booking in self.bookings:
            print(f"{booking['ticket_id']}: {booking['passenger']} | {booking['from']} to {booking['to']} | Class: {booking['class']} | Fare: ${booking['fare']} | Status: {booking['status']}")

    def get_status(self):
        print(f"\nTrain {self.trainno} is currently: On Time\n")

    def fare_info(self):
        print(f"\nFare Info:")
        print(f"From: {self.fro}")
        print(f"To: {self.to}")
        print(f"Class: {self.class_type}")
        print(f"Estimated Fare: ${self.fare}\n")

def main():
    train = Train("12345", "PUNE", "MUMBAI", "AC")
    while True:
        print("\n====== TRAIN BOOKING SYSTEM ======")
        print("1. Book Ticket")
        print("2. View Bookings")
        print("3. Check Train Status")
        print("4. Fare Info")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter passenger name: ")
            train.book_ticket(name)

        elif choice == "2":
            train.view_bookings()

        elif choice == "3":
            train.get_status()

        elif choice == "4":
            train.fare_info()

        elif choice == "5":
            print("\nThank you for using the Train Booking System")
            break

        else:
            print("Invalid input. Please choose between 1-5.")

        time.sleep(1.5)

if __name__ == "__main__":
    main()
