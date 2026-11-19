import hotel_data
import rooms
import bookings


# Display menu options
def show_menu():
    print(f"\n****** {hotel_data.HOTEL_NAME} Booking System ******")
    print("1. View rooms")
    print("2. Book a room")
    print("3. View all bookings")
    print("4. Cancel a booking")
    print("5. Exit")

def main():
    running = True

    # Looping through the menu until the user exit
    while running:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            rooms.show_rooms()
        elif choice == "2":
            bookings.book_room()
        elif choice == "3":
            bookings.view_bookings()
        elif choice == "4":
            bookings.cancel_booking()
        elif choice == "5":
            print("Thank you for using the system. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Only run main() when this file is run directly
if __name__ == "__main__":
    main()