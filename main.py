import customtkinter as ctk
import pretty_errors
#import my_library

english_verb = ["answer", "work", "begin", "get", "use", "visit", "pay", "stay", "need", "last", "think", "discover", "invent", "complete", "permit", "tell", "eat", "find", "fish", "fly", "ask", "go", "win", "believe", "help", "buy", "know", "come", "run", "teach", "learn", "love", "lay", "make", "happen", "smoke", "travel", "run2", "call", "say", "sleep", "write", "swim", "see", "sing", "sit", "save", "put", "stand", "study", "lookfor", "dance", "meet", "separate", "drink", "earn", "forget", "lose", "promise", "understand", "wait", "wash", "wave", "wipe", "wish", "move"]
german_verb = ["antworten", "arbeiten", "beginnen", "bekommen", "benutzen", "besuchen", "bezahlen", "bleiben", "brauchen", "dauern", "denken", "entdecken", "erfinden", "erganzen", "erlauben", "erzahlen", "essen", "finden", "fischen", "fliegen", "fragen", "gehen", "gewinnen", "glauben", "helfen", "kaufen", "kennen", "kommen", "laufen", "lehren", "lernen", "lieben", "liegen", "machen", "passieren", "rauchen", "reisen", "rennen", "rufen", "sagen", "schlafen", "schreiben", "schwimmen", "sehen", "singen", "sitzen", "sparen", "stecken", "stehen", "studieren", "suchun", "tanzen", "treffen", "trennen", "trinken", "verdienen", "vergessen", "verlieren", "versprechen", "verstehen", "warten", "waschen", "winken", "wischen", "wunschen", "ziehen"]


def translate(word_in):
    answer = "not found"  # Default answer if the word is not found
    for i in range(len(english_verb)):
        if word_in == english_verb[i]:
            answer = german_verb[i]
            break
        elif word_in == german_verb[i]:
            answer = english_verb[i]
            break
    return answer

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class TranslatorApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Jenepher Translator")
        self.geometry("400x200")

        # Create widgets
        self.label = ctk.CTkLabel(self, text="Enter an English or German verb:")
        self.entry = ctk.CTkEntry(self)
        self.translate_button = ctk.CTkButton(self, text="Translate", command=self.translate)
        self.translation_label = ctk.CTkLabel(self, text="Translation will appear here :", font=("Arial", 10, "italic"))

        # Grid layout
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.entry.grid(row=0, column=1, padx=10, pady=10)
        self.translate_button.grid(row=1, columnspan=2, padx=10, pady=10)
        self.translation_label.grid(row=2, columnspan=2, padx=10, pady=10)

    def translate(self):
        word_in = self.entry.get().lower()
        translation = translate(word_in)
        if translation != "not found":
            self.translation_label.configure(text=f"Translation : {translation}")
        else:
            self.translation_label.configure(text="Word not found in dictionary.")

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()

##print_translation('verb')
