import tkinter as tk
import time
from utils.logic import calculate_speed, calculate_accuracy
from utils.texts import get_random_text

class TypingSpeedTest:
    """Class to handle the Typing Speed Test GUI and logic."""

    def __init__(self, root):
        """
        Initialize the Typing Speed Test application.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.sample_text = get_random_text()
        self.start_time = None

        self.label = tk.Label(root, text="Type the following text as fast as you can:")
        self.label.pack()

        self.sample_label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.sample_label.pack()

        self.text_entry = tk.Text(root, height=5, width=50)
        self.text_entry.pack()
        self.text_entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.time_label = tk.Label(root, text="Time: 0.00 seconds")
        self.time_label.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_speed)
        self.submit_button.pack()

        self.new_text_button = tk.Button(root, text="New Text", command=self.select_new_text)
        self.new_text_button.pack()

    def start_timer(self, event):
        """Start the timer when the user begins typing."""
        if self.start_time is None:
            self.start_time = time.time()
            self.update_time()

    def update_time(self):
        """Update the displayed time every 100 milliseconds."""
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {elapsed_time:.2f} seconds")
            self.root.after(100, self.update_time)

    def calculate_speed(self):
        """
        Calculate the typing speed and accuracy.

        Raises:
            ValueError: If the start time is None.
        """
        if self.start_time is None:
            raise ValueError("Timer has not been started.")

        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.text_entry.get("1.0", tk.END).strip()

        words_per_minute = calculate_speed(typed_text, time_taken)
        accuracy = calculate_accuracy(self.sample_text, typed_text)

        self.result_label.config(text=f"Speed: {words_per_minute:.2f} WPM\nAccuracy: {accuracy:.2f}%")
        self.start_time = None

        # Reset the text entry
        self.text_entry.delete("1.0", tk.END)

    def select_new_text(self):
        """Select a new sample text for the typing test."""
        self.sample_text = get_random_text()
        self.sample_label.config(text=self.sample_text)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.time_label.config(text="Time: 0.00 seconds")
        self.start_time = None