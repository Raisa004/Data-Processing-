name = input("Enter passenger name: ")
destination = input("Enter destination: ")
ticket_count = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (adult/child/student/senior): ")


if destination == "Dhaka":
    fare = 80
elif destination == "Chittagong":
    fare = 160
elif destination == "Sylhet":
    fare = 120
else:
    fare = 100

if passenger_type == "child":
    discount = 0.50
elif passenger_type == "student":
    discount = 0.20
elif passenger_type == "senior":
    discount = 0.30
else:
    discount = 0


fare_after_discount = fare - (fare * discount)
total_fare = fare_after_discount * ticket_count

print("Passenger:", name)
print("Destination:", destination)
print("Passenger Type:", passenger_type)
print("Number of Tickets:", ticket_count)
print("Fare per Ticket:", fare)
print("Discount:", discount * 100, "%")
print("Total Fare:", total_fare)
