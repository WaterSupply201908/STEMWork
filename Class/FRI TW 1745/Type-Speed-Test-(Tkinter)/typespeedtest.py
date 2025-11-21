from tkinter import *
import json, time, random

class TypingTest :
    def __init__(self, root) :
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")

        with open("words.json", "r", encoding='utf-8') as file :
            self.test_data = json.load(file)

        self.current_text = ''
        self.start_time = 0
        self.is_testing = False
        self.timer_running = False

        self.create_widgets()
        self.load_new_text()

    def create_widgets(self) :
        self.text_label = Label(self.root, text='', font=('Arial', 18), wraplength=700, justify=LEFT)
        self.text_label.pack(pady=20)

        self.input_text = Text(self.root, height=5, width=80, font=('Arial', 16))
        self.input_text.pack(pady=10)

        self.input_text.tag_configure("correct", foreground="green")
        self.input_text.tag_configure("wrong", foreground="red")

        self.input_text.bind('<Key>', self.check_typing)

        self.reset_button = Button(self.root, text="New Text", command=self.reset_text, font=('Arial', 12))
        self.reset_button.pack(pady=10)

        self.result_frame = Frame(self.root)
        self.result_frame.pack(pady=20)

        self.speed_label = Label(self.result_frame, text='Speed: 0 WPM', font=('Arial', 14))
        self.speed_label.pack(side=LEFT, padx=10)

        self.accuracy_label = Label(self.result_frame, text='Accuracy: 0%', font=('Arial', 14))
        self.accuracy_label.pack(side=LEFT, padx=10)

        self.time_label = Label(self.result_frame, text='Time: 0 seconds', font=('Arial', 14))
        self.time_label.pack(side=LEFT, padx=10)

        self.status_label = Label(self.root, text='Start typing to begin the test...', font=('Arial', 12))
        self.status_label.pack(pady=5)

    def load_new_text(self) :
        self.current_text = random.choice(self.test_data['texts'])
        self.text_label.config(text=self.current_text)
        self.input_text.delete(1.0, END)
        self.is_testing = False
        self.timer_running = False

    def start_timer(self) :
        if not self.timer_running :
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self) :
        if self.timer_running :
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f'Time: {elapsed_time:.1f} seconds')

            if self.is_testing :
                typed_text = self.input_text.get(1.0, END).strip()
                wpm = self.calculate_wpm(typed_text, elapsed_time)
                self.speed_label.config(text=f'Speed: {wpm:.1f} WPM')

            self.root.after(100, self.update_timer)

    def calculate_wpm(self, text, time_in_seconds) :
        pass

    def reset_text(self) :
        pass

    def check_typing(self, event) :
        pass

    def end_test(self) :
        pass

# Main
if __name__ == "__main__" :
    root = Tk()
    app = TypingTest(root)
    root.mainloop()
