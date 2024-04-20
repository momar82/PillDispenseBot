import tkinter as tk
import netifaces
import time

def get_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addresses = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addresses:
            for addr_info in addresses[netifaces.AF_INET]:
                ip = addr_info['addr']
                if ip != '127.0.0.1':
                    return ip
    return 'No IP found'

def update_label():
    ip_label.config(text="IP: " + get_ip())
    root.after(1000, update_label)

def countdown():
    global timer
    countdown_label.config(text="Countdown: " + str(timer))
    if timer > 0:
        timer -= 1
        root.after(1000, countdown)
    else:
        alarm()

def alarm():
    global default_bg
    for _ in range(3):  # Beep three times
        root.bell()
        time.sleep(0.5)
    reset_button.config(state=tk.NORMAL)
    input_text.config(state=tk.NORMAL)
    default_bg = root.cget('bg')  # Save default background color
    root.configure(bg="red")  # Change background color to red

def reset():
    global timer
    timer = 5  # Reset timer to 5 seconds
    countdown_label.config(text="Countdown: " + str(timer))
    reset_button.config(state=tk.DISABLED)  # Disable reset button
    root.configure(bg=default_bg)  # Reset background color
    input_text.config(state=tk.DISABLED)  # Disable text input
    countdown()  # Start countdown again

def check_input(event=None):
    input_value = input_text.get()
    if input_value == "12345678":
        root.configure(bg="green")  # Change background color to green
     
        reset()
    else:
        print("Incorrect message entered!")

root = tk.Tk()
root.title("IP Address and Countdown Timer")
root.geometry("400x250")

timer = 5  # Start countdown from 5 seconds
default_bg = root.cget('bg')  # Get default background color

ip_label = tk.Label(root, font=("Helvetica", 24))
ip_label.pack()

countdown_label = tk.Label(root, font=("Helvetica", 24))
countdown_label.pack()

update_label()
countdown()

reset_button = tk.Button(root, text="Reset", command=reset, state=tk.DISABLED)
reset_button.pack()

input_text = tk.Entry(root, font=("Helvetica", 14), state=tk.DISABLED)
input_text.pack()
input_text.bind("<Return>", check_input)  # Bind Enter key to check_input function

root.mainloop()
