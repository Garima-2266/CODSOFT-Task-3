import tkinter as tk
import random
import time

class TypingSpeedTester(tk.Tk):
    def __init__(self):
        super().__init__()

        self.words = ["Hello world, Welcome to typingspeed tester!", "Python", "Speed", "Tester"]
        self.current_word = ""
        self.start_time = None

        self.title("Typing Speed Tester")
        self.geometry("400x200")
        self.configure(bg="black")

        self.word_label = tk.Label(self, text="", font=("Arial", 24), bg="black", fg="white")
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.result_label = tk.Label(self, text="", font=("Arial",16), bg="black", fg="white")
        self.result_label.pack(pady=20)

        self.get_new_word()

    def get_new_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.start_time = time.time()

    def check_word(self,event):
        typed_word = self.entry.get().strip()
        if typed_word == self.current_word:
            elapsed_time = time.time() - self.start_time
            wpm = int(len(self.current_word)/(elapsed_time/60))
            self.result_label.config(text=f"Your typing speed is: {wpm} WPM", fg="white")
        else:
            self.result_label.config(text="Wrong word try again!", fg="white")

            self.after(1500, self.get_new_word)

if __name__ == "__main__":
            app = TypingSpeedTester()
            app.mainloop()



