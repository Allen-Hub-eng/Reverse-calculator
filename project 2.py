import tkinter as tk
import random

# List of fun or sarcastic messages
messages = [
    "You're basically a math wizard now. 🧙",
    "This definitely won't help you pass any exams. 🤓",
    "Math just gave up and said okay. 🙃",
    "Weirdly accurate. Emotionally wrong. 😵‍💫",
    "Don't question the logic. Just accept it. 🤷‍♂️",
    "Albert Einstein would be... confused. 🧠",
    "Why? Because we can. 💅",
    "This is exactly how NASA does it. Probably. 🚀",
    "You've reached peak productivity. 🎉",
    "This expression deserves a TED Talk. 🎤"
]

# Function to generate a weird expression
def generate_expression(target):
    attempts = 0
    while attempts < 1000:
        a = random.randint(-50, 50)
        b = random.randint(-50, 50)
        c = random.randint(-50, 50)
        d = random.randint(1, 10)

        # Try a few random formats
        if a + b - c == target:
            return f"(({a} + {b}) - {c})"
        if a * d + b - c == target:
            return f"(({a} × {d}) + {b} - {c})"
        if (a - b) * d + c == target:
            return f"(({a} - {b}) × {d} + {c})"
        attempts += 1
    return "Expression too weird to compute 😅"

# Function to handle button press
def on_generate():
    try:
        target = int(entry.get())
        expr = generate_expression(target)
        msg = random.choice(messages)
        result_label.config(text=f"{expr} = {target}")
        message_label.config(text=msg)
    except ValueError:
        result_label.config(text="That's not even a number! 🤦")
        message_label.config(text="Try again, math rebel.")

# Set up GUI
root = tk.Tk()
root.title("🌀 Reverse Calculator (Useless Edition)")
root.geometry("450x250")
root.resizable(False, False)

title = tk.Label(root, text="Enter a number below:", font=("Helvetica", 20))
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 20), justify='center')
entry.pack(pady=5)

generate_button = tk.Button(root, text="🎲 FOOL ME", font=("Helvetica", 20), command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 16), fg="purple")
result_label.pack(pady=5)

message_label = tk.Label(root, text="", font=("Helvetica", 15), fg="black")
message_label.pack(pady=5)

root.mainloop()
