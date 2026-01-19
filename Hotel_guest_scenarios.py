
#Here we are creating a guest file and writing the list of guests present in hotel

guests = open("guests.txt","w")
#we created guest file and opened it in write mode
initial_guests = ["Bob", "Sam", "Jerry", "Cherry"]
#we create a list of initial guests
for i in initial_guests:
    guests.write(i+"\n")

#we used a for loop to traverse through initial guest list and write the, to the guests file

guests.close()
#we then close the guest file

with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())

#we are printing the guest list which we stored in guests.txt file early


#lets create a new list which has new  users checking in the hotel
new_guests = ["Radha", "Krishna", "Shyam", "Ram"]

with open("guests.txt", "a") as file:
    for i in new_guests:
        file.write(i+"\n")

guests.close()

print("\n")

with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())


#Now Lets remove some guests who have checked out from the hotel

print("\n")

checked_out =["Krishna", "Sam"]
temp_list = []
with open("guests.txt", "r") as file:
    for line in file:
        temp_list.append(line.strip())

#print(temp_list)
#we created a temporary list with all the guests from the guests.txt file
#then we opened the guests file in write mode to completely rewrite the file while iterating through
#temporaryl list and checking if checked out user is in the temporary list or not

with open("guests.txt", "w") as file:
    for name in temp_list:
        if name not in checked_out:
            file.write(name+"\n")


with open("guests.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n")

#now we will check for guest who has checkedin or has checked out
guest_to_check = ["Krishna", "Bob"]
checked_in = []

with open("guests.txt", "r") as file:
    for line in file:
        checked_in.append(line.strip())

    for name in guest_to_check:
        if name in checked_in:
            print(f" {name} is checked in")
        else:
            print(f" {name} is not checked in")
