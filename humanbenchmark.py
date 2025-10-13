import pyautogui
import pyscreeze
import time
import tkinter as tk
import threading

# Define the target color to detect (green)
tcolor = (75, 219, 106)
bot_running = False

# Bot logic
def start_bot():
    global bot_running
    bot_running = True
    status_label.config(text="Bot is running...", fg="green")
    while bot_running:
        color = pyautogui.pixel(320, 360)
        print(color)
        if color == tcolor:
            pyautogui.click(320, 360) # clicks green
            pyautogui.click(320, 360) # clicks again to start over

# Start the bot in a separate thread to keep GUI responsive
def run_bot_thread():
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

# Stop the bot loop
def stop_bot():
    global bot_running
    bot_running = False
    status_label.config(text="Bot stopped.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Reaction Time Bot")
root.geometry('400x350')
root.configure(bg="#f0f0f0")

# Fonts
title_font = ("Helvetica", 16, "bold")
button_font = ("Helvetica", 12)
label_font = ("Helvetica", 10)

# Title
title_label = tk.Label(root, text="Reaction Time Bot", font=title_font,bg="#f0f0f0")
title_label.pack(pady=(20, 10))

# Description
desc_label = tk.Label(root, text="Automates Humanbenchmark Reaction Time test", font=label_font, bg="#f0f0f0")
desc_label.pack(pady=(0, 20))

# Buttons
start_button = tk.Button(root, text="▶ Start Bot", font=button_font, width=15, bg="#d1e7dd", command=run_bot_thread)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="⏹ Stop Bot", font=button_font, width=15, bg="#f8d7da", command=stop_bot)
stop_button.pack(pady=5)

# Status label
status_label = tk.Label(root, text="Bot is idle.", font=label_font, bg="#f0f0f0", fg="gray")
status_label.pack(pady=(20, 10))

credit = tk.Label(root, text="By offlanity.", font=label_font, bg="#f0f0f0", fg="gray")
credit.pack(pady=(20, 10))
root.mainloop()