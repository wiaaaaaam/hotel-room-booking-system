import hotel_data
import rooms
import receipt
import validation

# Take guest details, check the room and save the booking
def book_room():
    rooms.show_rooms()
    room_number = validation.get_number("\nEnter room number to book: ")
    room = rooms.find_room(room_number)

    # check that the room exists and is free
    if room is None:
        print("Room not found. Please check the room number.")
        return
    if not room["available"]:
        print(f"Sorry, room {room_number} is already booked.")
        return

    guest_name = validation.get_name("Enter guest name: ")
    nights = validation.get_number("Enter number of nights: ")
    total = receipt.calculate_total(room["price"], nights)

    # Store the booking as a dictionary and add it to the bookings list
    booking = {
        "guest": guest_name,
        "room": room_number,
        "type": room["type"],
        "nights": nights,
        "total": total,
    }
    hotel_data.bookings.append(booking)
    rooms.set_availability(room_number, False)

    receipt.print_receipt(booking)

# Show all bookings made
def view_bookings():
    if len(hotel_data.bookings) == 0:
        print("\nNo bookings yet.")
        return

    print("\n------------- ALL BOOKINGS -------------")
    count = 1
    for booking in hotel_data.bookings:
        print(f"{count}. {booking['guest']} - Room {booking['room']} "
              f"({booking['type']}), {booking['nights']} night(s), "
              f"RM {booking['total']:.2f}")
        count += 1

# Return the booking for a room number, or None if there is no booking
def find_booking(room_number):
    for booking in hotel_data.bookings:
        if booking["room"] == room_number:
            return booking
    return None

#  Cancel a booking by room number
def cancel_booking():
    if len(hotel_data.bookings) == 0:
        print("\nThere are no bookings to cancel.")
        return

    room_number = validation.get_number("Enter room number to cancel: ")
    booking = find_booking(room_number)

    if booking is None:
        print("No booking found for that room.")
        return

    if validation.get_yes_no(f"Cancel booking for {booking['guest']}? (y/n): "):
        hotel_data.bookings.remove(booking)
        rooms.set_availability(room_number, True)
        print("Booking cancelled.")
    else:
        print("Cancellation stopped.")