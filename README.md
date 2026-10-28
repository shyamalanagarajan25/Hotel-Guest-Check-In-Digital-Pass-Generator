Hotel Guest Check-In & Digital Pass Generator

A desktop app built with Python and Tkinter that lets a hotel front desk check in a guest, print a reservation receipt, and generate a QR code digital room pass in one click.

✨ Features

Guest registration form (name and phone number)
Room category dropdown: Deluxe Suite, Executive King, Standard Twin, Presidential Suite
Add-on services: Wi-Fi, Breakfast, Cab Pickup
Payment method selection: Card / UPI, Cash, Pay at Checkout
Input validation with error pop-ups
Auto-generated reservation receipt
QR code Digital Room Pass shown inside the app
One-click Reset for the next guest
Tech Stack
Python 3
Tkinter / ttk (GUI)
qrcode (QR generation)
Pillow (image handling)
Getting Started
1. Clone the repository
bash
git clone https://github.com/<your-username>/hotel-checkin-app.git
cd hotel-checkin-app
2. Install dependencies
bash
pip install qrcode pillow

Tkinter comes with Python. On Linux, install it with sudo apt install python3-tk if needed.

3. Run the app
bash
python Hotel_booking.py

📖 How to Use

Enter the guest's name and phone number.
Choose a room category, add-on services, and payment method.
Click Confirm & Generate Pass.
View the reservation receipt and the QR room pass.
Click Reset to start a new check-in.

How It Works

When you click Confirm & Generate Pass, the app checks that name and phone are filled in, builds a formatted receipt from the form values, and encodes the guest name, room, and payment mode into a QR code using the qrcode library. Pillow resizes the image so Tkinter can display it in the Digital Room Pass panel.

📁 Project Structure

hotel-checkin-app/
├── Hotel_booking.py   # Main application
└── README.md

🔮 Future Improvements

Store guest records in SQLite or MySQL
Add check-in/check-out dates and automatic bill calculation
Export receipt as PDF and save the QR code as an image
Add staff login
Build a bookings dashboard in Power BI

👩‍💻 Author

Shyamala Devi N
