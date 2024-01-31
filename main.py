import tkinter as tk
import random
import keyboard
import time
from phrases_list import phrases_to_practice


def calculate_speed(words, end_time):
    words_per_minute = (words / end_time) * 60
    return words_per_minute


class SpeedTyping:
    def __init__(self, window_screen, list_words):
        self.window = window_screen
        self.list_words = list_words
        self.typed_words = ""
        self.window.geometry("1000x500")
        self.window.config(bg="#42c8f5")
        self.words_typed = []

        self.word = (
            tk.Label(text=self.list_words, bg="#42c8f5", fg="white", font=('Times New Roman', 20, 'bold'), height=8, ))
        self.word.pack()
        self.typed_entry = tk.Entry(width=100)
        self.typed_entry.pack()
        self.typed_entry.focus_set()
        keyboard.hook(self.on_key_event)
        self.result_words = tk.Label(text="")
        self.result_words.pack()
        self.start = time.time()
        self.count = 0
        self.total_words = len(self.list_words.split())

    def check_letter(self):
        if not self.typed_words:
            return
        typed_leter = self.typed_words[-1] if self.typed_words else " "
        reference_leter = self.list_words[len(self.typed_words) - 1] if (len(self.typed_words)
                                                                         <= len(self.list_words)) else " "
        if typed_leter == reference_leter or (typed_leter == " " and reference_leter == " "):
            self.result_words.config(text=typed_leter, fg="green", font=("Market", 15, "bold"))
            self.count += 1
        else:
            self.result_words.config(text=typed_leter, fg="red", font=("Market", 15, "bold"))
            self.count -= 1

    def stop_time(self):
        finish = time.time()
        end_time = finish - self.start

        if self.typed_words.strip():
            words = len(self.typed_words.split())
            speed = calculate_speed(words=words, end_time=end_time)
            accuracy_percentage = (self.count / self.total_words) * 100
            result_time = tk.Label(text=f"You have typed in {end_time:.2f} seconds")
            result_time.pack()
            result_time_per_word = tk.Label(text=f"Your speed of typing in approximate {speed:.2f} words per second\n"
                                                 f"Your accuracy is {accuracy_percentage:.2f}%\n"
                                                 f"and your end points are {self.count}")
            result_time_per_word.pack()

    def on_key_event(self, e):
        if e.event_type == keyboard.KEY_DOWN:
            if e.name == "enter":
                self.stop_time()
            elif e.name == "space":
                self.typed_words += " "
                self.words_typed += " "
            elif e.name == "shift" or e.name == "capslock":
                pass
            elif e.name == "backspace" or e.name == "delete":
                if self.typed_words:
                    self.typed_words = self.typed_words[:-1]
                    self.typed_entry.delete(0, tk.END)
                    self.typed_entry.insert(tk.END, self.typed_words)
                    self.check_letter()

            else:
                self.typed_words += e.name
                self.typed_entry.delete(0, tk.END)
                self.typed_entry.insert(tk.END, self.typed_words)
                self.check_letter()


if __name__ == "__main__":
    window = tk.Tk()
    game = SpeedTyping(window_screen=window, list_words=random.choice(phrases_to_practice))
    window.mainloop()
