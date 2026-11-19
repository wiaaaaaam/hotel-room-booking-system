import hotel_data

# Return the total cost of a stay
def calculate_total(price_per_night, nights):
    return price_per_night * nights

# Print a simple receipt for one booking
def print_receipt(booking):
    print("\n******** BOOKING RECEIPT ********")
    print(f"Hotel      : {hotel_data.HOTEL_NAME}")
    print(f"Guest      : {booking['guest']}")
    print(f"Room       : {booking['room']} ({booking['type']})")
    print(f"Nights     : {booking['nights']}")
    print(f"Total (RM) : {booking['total']:.2f}")
    print("*************************************")
    print("Booking successful. Thank you!")