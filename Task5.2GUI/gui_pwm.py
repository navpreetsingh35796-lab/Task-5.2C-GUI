import tkinter as tk
import RPi.GPIO as GPIO

# --- Hardware Configuration ---
LED_PIN = 18  # BCM 18 / Physical Pin 12 (PWM0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Set PWM frequency to 1000 Hz
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)  # Start with light OFF (0% duty cycle)

# --- Functions ---
def update_intensity(val):
    """Update PWM duty cycle whenever slider is moved."""
    duty = float(val)
    pwm.ChangeDutyCycle(duty)

def close_app():
    """Clean exit handler to safely reset GPIO pins."""
    pwm.stop()
    GPIO.cleanup()
    root.destroy()

# --- GUI Construction ---
root = tk.Tk()
root.title("Living Room Lighting Controller")
root.geometry("360x220")
root.resizable(False, False)

title_label = tk.Label(
    root, 
    text="Living Room Light", 
    font=("Helvetica", 14, "bold")
)
title_label.pack(pady=12)

instruction_label = tk.Label(
    root, 
    text="Adjust Intensity Level (0 - 100%):", 
    font=("Helvetica", 10)
)
instruction_label.pack()

# Slider widget (Scale)
intensity_slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=260,
    command=update_intensity
)
intensity_slider.set(0)
intensity_slider.pack(pady=10)

# Exit button
exit_btn = tk.Button(
    root, 
    text="Exit", 
    width=12, 
    command=close_app
)
exit_btn.pack(pady=10)

# Handle window close (X button) safely
root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
