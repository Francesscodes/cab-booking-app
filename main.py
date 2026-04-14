class Cab:
    
    # Initialize cab details
    def __init__(self, cab_id, driver_name, rate_per_km):
        self.cab_id = cab_id
        self.driver_name = driver_name
        self.rate_per_km = rate_per_km
        self.is_available = True

    # Show cab info
    def show_info(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Cab ID: {self.cab_id}, Driver: {self.driver_name}, Rate per km: {self.rate_per_km}, Status: {status}")


class Booking:

    # Initialize booking manager with cab list
    def __init__(self):
        self.cabs = [
            Cab(1, "Emeka", 15),
            Cab(2, "Musa", 18),
            Cab(3, "Donald", 20)
        ]

    # Display all cabs
    def show_all_cabs(self):
        print("\nAvailable Cabs:")
        for cab in self.cabs:
            cab.show_info()

    # Book a cab
    def book_cab(self):
        cab_id = int(input("Enter cab ID to book: "))
        distance = float(input("Enter distance (km): "))
        for cab in self.cabs:
            if cab.cab_id == cab_id:
                if cab.is_available:
                    fare = distance * cab.rate_per_km
                    cab.is_available = False
                    print(f"Cab booked! Fare: #{fare}")
                else:
                    print("Cab is not available.")
                return
        print("Invalid cab ID.")

    # Cancel a booking
    def cancel_booking(self):
        cab_id = int(input("Enter cab ID to cancel booking: "))
        for cab in self.cabs:
            if cab.cab_id == cab_id:
                if not cab.is_available:
                    cab.is_available = True
                    print("Booking cancelled.")
                else:
                    print("Cab is not booked.")
                return
        print("Invalid Cab ID.")


# Run the CLI menu
def main():
    booking = Booking()

    while True:
        print("\n--- Cab Booking Menu ---")
        print("1. Show All Cabs")
        print("2. Book a Cab")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            booking.show_all_cabs()
        elif choice == '2':
            booking.book_cab()
        elif choice == '3':
            booking.cancel_booking()
        elif choice == '4':
            print("Thank you for using Cab Booking App.")
            break
        else:
            print("Invalid choice. Try again.")


# Entry point of the app
if __name__ == "__main__":
    main()