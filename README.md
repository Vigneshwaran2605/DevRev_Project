# Flight Ticket Booking(AEROBOOK)

This project is developed by using Django as backend and HTML as frontend. Django files are stored inProject1/backend/users/ and HTML files are stored in the Project1/backend/users/templates. My output is recorded and uploaded in https://drive.google.com/drive/folders/1g9-OZ3gTnSb47DMAu9hp4d7uuZndRwqs?usp=sharing

# To run this project in local server, follow the given steps:-

1. Download the project by using command "git clone https://github.com/Vigneshwaran2605/DevRev_Project.git".
2. Install Django by using the command "pip install django".
3. Run the Django server with 'python manage.py runserver' command from the Project1\backend folder.
4. The project runs on http://127.0.0.1:8000/ in your browser.

# Problem Statement:-

## Flight Ticket Booking 

1. Type of Users : 
a. User
b. Admin

2. User Use Cases : 
● Login
● Sign up
● Searching for flights based on date and time
● Booking tickets on a flight based on availability (assuming the default
seat count is 60)
● My Booking -&gt; to list out all the bookings made by that user
● Logout

3. Admin Use Cases: 
● Login (Seperate login for Admin)
● Add Flights
● Remove flights
● View all the booking based on flight number and time

# Features of the Flight Ticket Booking(AEROBOOK):-

1. Login Page -> Enter username and password for sigin and there is seperate login for admin
2. Signup Page -> Enter details for registeraccount
3. Logout -> Signout from the account.

## User Side

1. Search Flight -> Search the flight by date and time
2. Book Flight -> Book the flight by search with date and time and check if there is availability of seats
3. My Bookings -> Show the list of all bookings made by user.
4. Show Flight -> Show the list of all available flights.
5. Cancel Flight -> Cancel the booked ticket by entering booking ID.

## Admin Side

1. Add Flight -> Add Flight by entering date,time and seat availability.
2. Remove Flight -> Remove Flight by entering Flight ID.
3. View Bookings -> View all the bookings made to the specific Flight ID , it list as the username and seats booked.
4. Show Flight -> Show the list of all the flights.

