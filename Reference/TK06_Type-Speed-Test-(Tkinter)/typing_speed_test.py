from tkinter import *
import json
import time
import random

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        
        # Load test texts
        with open('typing_test_data.json', 'r', encoding='utf-8') as file:
            self.test_data = json.load(file)
        
        # Initialize variables
        self.current_text = ""
        self.start_time = 0
        self.is_testing = False
        self.timer_running = False
        
        # Create interface
        self.create_widgets()
        self.load_new_text()
    
    def create_widgets(self):
        # Display test text
        self.text_label = Label(self.root, text="", font=("Arial", 18), wraplength=700, justify=LEFT)
        self.text_label.pack(pady=20)
        
        # Input box
        self.input_text = Text(self.root, height=5, width=80, font=("Arial", 16))
        self.input_text.pack(pady=10)
        
        # Configure color tags
        self.input_text.tag_configure("correct", foreground="green")
        self.input_text.tag_configure("wrong", foreground="red")
        
        # Bind key event
        self.input_text.bind('<Key>', self.check_typing)
        
        # Reset button
        self.reset_button = Button(self.root, text="New Text", command=self.reset_test, font=("Arial", 12))
        self.reset_button.pack(pady=10)
        
        # Results display
        self.result_frame = Frame(self.root)
        self.result_frame.pack(pady=20)
        
        self.speed_label = Label(self.result_frame, text="Speed: 0 WPM", font=("Arial", 14))
        self.speed_label.pack(side=LEFT, padx=10)
        
        self.accuracy_label = Label(self.result_frame, text="Accuracy: 0%", font=("Arial", 14))
        self.accuracy_label.pack(side=LEFT, padx=10)
        
        self.time_label = Label(self.result_frame, text="Time: 0 seconds", font=("Arial", 14))
        self.time_label.pack(side=LEFT, padx=10)
        
        # Status label
        self.status_label = Label(self.root, text="Start typing to begin the test...", font=("Arial", 12))
        self.status_label.pack(pady=5)
    
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()
    
    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {elapsed_time:.1f} seconds")
            
            if self.is_testing:
                typed_text = self.input_text.get(1.0, END).strip()
                wpm = self.calculate_wpm(typed_text, elapsed_time)
                self.speed_label.config(text=f"Speed: {wpm:.1f} WPM")
            
            self.root.after(100, self.update_timer)
    
    def calculate_wpm(self, text, time_in_seconds):
        words = len(text) / 5  # just assum that around 5 character per word(it's not true but it's just for fun and hard to calculate)
        minutes = time_in_seconds / 60
        return words / minutes if minutes > 0 else 0
    
    def load_new_text(self):
        self.current_text = random.choice(self.test_data["texts"])
        self.text_label.config(text=self.current_text)
        self.input_text.delete(1.0, END)
        self.is_testing = False
        self.timer_running = False
    
    def reset_test(self):
        # Reset variable
        self.is_testing = False
        self.timer_running = False
        self.start_time = 0
        
        # Clear input box
        self.input_text.config(state='normal')
        self.input_text.delete(1.0, END)
        
        # Load new text
        self.load_new_text()
        
        # Reset all
        self.status_label.config(text="Start typing to begin the test...")
        self.speed_label.config(text="Speed: 0 WPM")
        self.accuracy_label.config(text="Accuracy: 0%")
        self.time_label.config(text="Time: 0 seconds")
        
        # Clear color
        self.input_text.tag_remove("correct", "1.0", END)
        self.input_text.tag_remove("wrong", "1.0", END)
    
    def check_typing(self, event):
        if not self.is_testing:
            self.is_testing = True
            self.start_timer()
            self.status_label.config(text="Test in progress...")
        
        typed_text = self.input_text.get(1.0, END).strip()
        
        # Clear color tags
        self.input_text.tag_remove("correct", "1.0", END)
        self.input_text.tag_remove("wrong", "1.0", END)
        
        # Set colors
        for i, (typed_char, correct_char) in enumerate(zip(typed_text, self.current_text)):
            tag = "correct" if typed_char == correct_char else "wrong"
            self.input_text.tag_add(tag, f"1.{i}", f"1.{i+1}")
        
        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(typed_text, self.current_text) if a == b)
        accuracy = (correct_chars / len(self.current_text)) * 100 if self.current_text else 0
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
        
        # Check if complete
        if len(typed_text) >= len(self.current_text):
            self.end_test()
    
    def end_test(self):
        self.is_testing = False
        self.timer_running = False
        self.input_text.config(state='disabled')
        
        typed_text = self.input_text.get(1.0, END).strip()
        elapsed_time = time.time() - self.start_time
        
        wpm = self.calculate_wpm(typed_text, elapsed_time)
        correct_chars = sum(1 for a, b in zip(typed_text, self.current_text) if a == b)
        accuracy = (correct_chars / len(self.current_text)) * 100
        
        self.speed_label.config(text=f"Final Speed: {wpm:.1f} WPM")
        self.accuracy_label.config(text=f"Final Accuracy: {accuracy:.1f}%")
        self.time_label.config(text=f"Total Time: {elapsed_time:.1f} seconds")
        self.status_label.config(text="Test completed! Click 'New Text' for a new challenge.")

if __name__ == "__main__":
    root = Tk()
    app = TypingTest(root)
    root.mainloop() 
