import hotel_data

# Display every room with its type, price and status
def show_rooms():
    print("\n------------- ROOM LIST -------------")
    print(f"{'Room':<6}{'Type':<10}{'Price (RM)':<12}{'Status'}")
    print("-" * 37)
    for room in hotel_data.rooms:
        if room["available"]:
            status = "Available"
        else:
            status = "Booked"
        print(f"{room['number']:<6}{room['type']:<10}{room['price']:<12.2f}{status}")


# Search the rooms list
def find_room(room_number):
    for room in hotel_data.rooms:
        if room["number"] == room_number:
            return room
    return None

# Mark a room as available or booked
def set_availability(room_number, available):
    room = find_room(room_number)
    if room is not None:
        room["available"] = available