# Book&Ride - Unified Mobility and Hospitality Platform

A web application that combines ride-hailing, property rental, and hotel booking in one system.

Built with: Python, Django, JavaScript, jQuery, HTML, CSS, PostgreSQL

## Problem

In Cameroon and similar markets, users need three separate apps for three related needs:
1. Book a ride to the airport
2. Book a stay on arrival
3. Book a hotel for a business trip

This fragments user data, payments, and trust. Book&Ride solves it with one account, one wallet, and one booking flow.

## Key Features

### 1. Ride-Hailing (Uber-style)
- Rider requests a ride with pickup and destination
- Driver matching based on proximity and availability
- Real-time ride status: Requested, Accepted, On Trip, Completed
- Fare estimation based on distance and time
- Rider and driver ratings after each trip

### 2. Property Rental (Airbnb-style)
- Hosts list apartments and houses with photos, price per night, and amenities
- Guests search by city, date, guests, and price
- Booking calendar with availability blocking
- Host approval flow and guest reviews

### 3. Hotel Booking (Booking.com-style)
- Hotels and guesthouses list rooms with room types
- Search by city, check-in, check-out, and rooms
- Room inventory management to prevent double booking
- Booking confirmation and cancellation policy

### Shared Platform Features
- Single user authentication with roles: Guest / Rider, Host, Driver, Hotel Manager, Admin
- Unified booking dashboard for all three services
- Search and filtering with PostgreSQL full-text search
- Admin panel for user verification, listings moderation, and dispute handling

## My Contribution

This is my original design and implementation. No no-code scaffold used.

- Designed the Django project structure with separate apps: accounts, rides, stays, hotels, bookings, payments
- Designed PostgreSQL schema for users, listings, rides, bookings, reviews, and payments
- Implemented role-based access control in Django views and templates
- Implemented booking logic to prevent double booking for stays and hotel rooms
- Implemented driver matching logic and ride state machine
- Built frontend with HTML, CSS, JavaScript, and jQuery for dynamic search and booking without page reloads

## Tech Stack

- Backend: Python 3.12, Django 5.x
- Frontend: HTML5, CSS3, JavaScript, jQuery, Bootstrap
- Database: PostgreSQL 16
- Auth: Django built-in auth with custom user model and role field
- Deployment: To be deployed on Render / Railway with Gunicorn

## Architecture

Browser (HTML / CSS / jQuery) -> Django Views / Templates -> Django ORM -> PostgreSQL
                                   -> Django Admin for moderation

- Rides app handles ride lifecycle
- Stays app handles property listings and availability
- Hotels app handles hotel rooms and inventory
- Bookings app is the central booking engine shared by all three

## Database Design Highlights

- CustomUser: id, email, phone, role, is_verified
- Ride: rider, driver, pickup_lat, pickup_lng, dropoff_lat, dropoff_lng, fare, status
- Property: host, title, city, price_per_night, max_guests, is_active
- HotelRoom: hotel, room_type, price_per_night, total_rooms, available_rooms
- Booking: user, booking_type (ride / stay / hotel), start_date, end_date, total_price, status
- Review: booking, reviewer, rating, comment

## How to Run Locally

```bash
git clone https://github.com/IbrahimBAko/BookRide.git
cd BookRide
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
