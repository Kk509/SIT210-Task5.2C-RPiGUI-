import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

root = tk.Tk()
root.title("LED control GUI")
root.geometry("400x300")

instructions_label = tk.Label(root, text="Select a color")
instructions_label.pack()

selected_color = tk.StringVar()

def on_color_selection():
        color = selected_color.get()
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        print("Selected color:", color)

        if color == "red":
                print("Turning on red LED")
                GPIO.output(17, GPIO.HIGH)
        elif color == "green":
                print("Turning on green LED")
                GPIO.output(22, GPIO.HIGH)
        elif color == "blue":
                print("Turning on blue LED")
                GPIO.output(27, GPIO.HIGH)

def close():
        GPIO.cleanup()
        root.destroy()


### WIDGETS ###
red_radio_button = tk.Radiobutton(root, text="Red", variable=selected_color, value="red", command=on_color_sele>
red_radio_button.pack()

green_radio_button = tk.Radiobutton(root, text="Green", variable=selected_color, value="green", command=on_colo>
green_radio_button.pack()

blue_radio_button = tk.Radiobutton(root, text="Blue", variable=selected_color, value="blue", command=on_color_s>
blue_radio_button.pack()

exit_button = tk.Button(root, text="Exit", command = close, bg = "red", height=1, width=24)
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", close) #exit cleanly
root.mainloop()

