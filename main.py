import tkinter as tk
import random
import winsound
import time

# Savage / funny reminders
messages = [
    "Oga, stand up! You no be tree 🌳",
    "Your chair don tire for your yansh, abeg stand up 😤",
    "Stretch small... before your body go resemble statue 🗿",
    "Guy, stand up! Even laptop dey rest sometimes 🔌",
    "Abeg respect yourself, 5 minutes no go kill you 😂",
    "Na so you go siddon till you turn office furniture? 🙄",
    "If you break your back, who go chop the money wey you dey hustle? 💸",
    "Stand up abeg, your body no be cement block 🚧",
    "No dey form hard guy, even Bruce Lee stretch 💪🏽",
    "Shey you dey plan to glue yourself to that chair? 😏",
    "Guy, blood suppose dey flow, no let your leg turn log of wood 🪵",
    "Omo, no dey stress me. Stand up sharp-sharp! 😡",
    "This chair dey suffer, free am small 😭",
    "Ahn ahn, your wahala don too much, STAND UP! 🚨",
    "Person fit fry akara for your back if you no stretch am now 😂",
    "No be punishment, na 5 minutes break. Do am like human being 🙃",
    "If I catch you still siddon, I go report you give physiotherapist 👩🏽‍⚕️",
]

def reminder():
    # Random savage message
    message = random.choice(messages)

    # Play sound alert (3 beeps)
    for _ in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.2)

    # Popup window
    root = tk.Tk()
    root.title("Take a Break!")

    label = tk.Label(root, text=message, font=("Arial", 16), padx=20, pady=20, wraplength=400)
    label.pack()

    button = tk.Button(root, text="Okay, I don hear 😅", command=root.destroy, padx=10, pady=5)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    reminder()
