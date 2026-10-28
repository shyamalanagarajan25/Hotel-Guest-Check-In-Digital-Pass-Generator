import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hotel Guest Check-In & Digital Pass Generator")
root.geometry("820x680")
root.configure(bg="#040335")

qr_photo_ref = None

def generate_pass():
    global qr_photo_ref
    
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    room_type = combo_room.get()
    payment = var_payment.get()
    
    selected_amenities = []
    if var_wifi.get():
        selected_amenities.append("High-Speed Wi-Fi")
    if var_breakfast.get():
        selected_amenities.append("Complimentary Breakfast")
    if var_pickup.get():
        selected_amenities.append("Airport Pickup")
        
    amenities_str = ", ".join(selected_amenities) if selected_amenities else "None"
    
    if not name or not phone:
        messagebox.showerror("Validation Error", "Please enter both Guest Name and Phone Number!")
        return

    summary = (
        "========================================\n"
        "       HOTEL GUEST CHECK-IN SUMMARY      \n"
        "========================================\n"
        f"Guest Name    : {name}\n"
        f"Contact No    : {phone}\n"
        f"Room Selected : {room_type}\n"
        f"Payment Mode  : {payment}\n"
        f"Amenities     : {amenities_str}\n"
        "Status        : Confirmed & Checked-In\n"
        "========================================\n"
    )
    
    text_summary.config(state="normal")
    text_summary.delete("1.0", tk.END)
    text_summary.insert(tk.END, summary)
    text_summary.config(state="disabled")
    
    #Generate QR Code
    qr_data = f"HOTEL-PASS | Name: {name} | Room: {room_type} | Pay: {payment}"
    qr_img = qrcode.make(qr_data)
    qr_img = qr_img.resize((150, 150))
    
    #Display QR Code Image in Label
    qr_photo_ref = ImageTk.PhotoImage(qr_img)
    label_qr_display.config(image=qr_photo_ref, text="")
    
    messagebox.showinfo("Success", "Guest checked in & QR Pass generated successfully!")

def reset_form():
    global qr_photo_ref
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    combo_room.current(0)
    var_wifi.set(False)
    var_breakfast.set(False)
    var_pickup.set(False)
    var_payment.set("Card / UPI")
    
    text_summary.config(state="normal")
    text_summary.delete("1.0", tk.END)
    text_summary.config(state="disabled")
    
    label_qr_display.config(image="", text="QR Pass will\nappear here")
    qr_photo_ref = None

# Header
header = tk.Label(
    root,
    text="🏨 Grand Plaza - Guest Check-In Portal",
    font=("Arial", 16, "bold"),
    bg="#2A3950",
    fg="white",
    pady=12
)
header.pack(fill="x")

# Form Frame 
form_frame = tk.LabelFrame(
    root,
    text=" Guest Registration Form ",
    font=("Arial", 11, "bold"),
    bg="#FFFFFF",
    padx=15,
    pady=15
)
form_frame.pack(padx=20, pady=10, fill="x")

# Name
tk.Label(form_frame, text="Guest Name:", font=("Arial", 10), bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=4)
entry_name = tk.Entry(form_frame, width=28, font=("Arial", 10))
entry_name.grid(row=0, column=1, padx=10, pady=4)

# Phone
tk.Label(form_frame, text="Phone Number:", font=("Arial", 10), bg="#FFFFFF").grid(row=0, column=2, sticky="w", padx=10, pady=4)
entry_phone = tk.Entry(form_frame, width=22, font=("Arial", 10))
entry_phone.grid(row=0, column=3, pady=4)

# Room Type (Combobox)
tk.Label(form_frame, text="Room Category:", font=("Arial", 10), bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=6)
combo_room = ttk.Combobox(
    form_frame,
    values=["Deluxe Suite", "Executive King", "Standard Twin", "Presidential Suite"],
    state="readonly",
    width=25
)
combo_room.current(0)
combo_room.grid(row=1, column=1, padx=10, pady=6)

# Amenities (Checkbuttons)
tk.Label(form_frame, text="Add-on Services:", font=("Arial", 10), bg="#FFFFFF").grid(row=2, column=0, sticky="w", pady=6)
var_wifi = tk.BooleanVar()
var_breakfast = tk.BooleanVar()
var_pickup = tk.BooleanVar()

check_box_frame = tk.Frame(form_frame, bg="#FFFFFF")
check_box_frame.grid(row=2, column=1, columnspan=3, sticky="w", padx=10)

tk.Checkbutton(check_box_frame, text="Wi-Fi", variable=var_wifi, bg="#FFFFFF").pack(side="left", padx=5)
tk.Checkbutton(check_box_frame, text="Breakfast", variable=var_breakfast, bg="#FFFFFF").pack(side="left", padx=5)
tk.Checkbutton(check_box_frame, text="Cab Pickup", variable=var_pickup, bg="#FFFFFF").pack(side="left", padx=5)

# Payment (Radiobuttons)
tk.Label(form_frame, text="Payment Method:", font=("Arial", 10), bg="#FFFFFF").grid(row=3, column=0, sticky="w", pady=6)
var_payment = tk.StringVar(value="Card / UPI")

radio_frame = tk.Frame(form_frame, bg="#FFFFFF")
radio_frame.grid(row=3, column=1, columnspan=3, sticky="w", padx=10)

tk.Radiobutton(radio_frame, text="Card / UPI", variable=var_payment, value="Card / UPI", bg="#FFFFFF").pack(side="left", padx=5)
tk.Radiobutton(radio_frame, text="Cash", variable=var_payment, value="Cash", bg="#FFFFFF").pack(side="left", padx=5)
tk.Radiobutton(radio_frame, text="Pay at Checkout", variable=var_payment, value="Pay at Checkout", bg="#FFFFFF").pack(side="left", padx=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#040335")
btn_frame.pack(pady=8)

tk.Button(
    btn_frame,
    text="✔ Confirm & Generate Pass",
    command=generate_pass,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=6
).pack(side="left", padx=10)

tk.Button(
    btn_frame,
    text="⟳ Reset",
    command=reset_form,
    bg="#C62828",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=6
).pack(side="left", padx=10)

# Display Area (Summary Box + QR Code Display)
bottom_frame = tk.Frame(root, bg="#F4F6F9")
bottom_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Left: Text Widget with Scrollbar
summary_frame = tk.LabelFrame(bottom_frame, text=" Reservation Receipt ", bg="#FFFFFF", padx=5, pady=5)
summary_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

scroll = tk.Scrollbar(summary_frame)
scroll.pack(side="right", fill="y")

text_summary = tk.Text(
    summary_frame,
    yscrollcommand=scroll.set,
    font=("Consolas", 10),
    bg="#FDFEFE",
    state="disabled"
)
text_summary.pack(fill="both", expand=True)
scroll.config(command=text_summary.yview)

# Right: QR Code Pass Box
qr_frame = tk.LabelFrame(bottom_frame, text=" Digital Room Pass ", bg="#FFFFFF", width=220)
qr_frame.pack(side="right", fill="y")
qr_frame.pack_propagate(False)

label_qr_display = tk.Label(
    qr_frame,
    text="QR Pass will\nappear here",
    font=("Arial", 9),
    bg="#ECEFF1",
    relief="groove"
)
label_qr_display.pack(expand=True, fill="both", padx=15, pady=15)

root.mainloop()