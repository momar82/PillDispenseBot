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
    for _ in range(3):  # Beep three times
        root.bell()
        time.sleep(0.5)
    reset_button.config(state=tk.NORMAL)

def reset():
    global timer
    timer = 10  # Reset timer to 10 seconds
    countdown_label.config(text="Countdown: " + str(timer))
    reset_button.config(state=tk.DISABLED)  # Disable reset button
    countdown()  # Start countdown again

root = tk.Tk()
root.title("IP Address and Countdown Timer")
root.geometry("400x200")

timer = 10

ip_label = tk.Label(root, font=("Helvetica", 24))
ip_label.pack()

countdown_label = tk.Label(root, font=("Helvetica", 24))
countdown_label.pack()

update_label()
countdown()

reset_button = tk.Button(root, text="Reset", command=reset, state=tk.DISABLED)
reset_button.pack()

root.mainloop()
