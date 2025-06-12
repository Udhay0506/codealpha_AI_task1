from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Main window setup
root = Tk()
root.title("🌐 Language Translator")
root.geometry("550x500")
root.configure(bg="lightblue")

translator = Translator()
languages = list(LANGUAGES.values())

# Set ttk styles
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 11), foreground='black', background='lightgray')
style.configure('TLabel', background='lightblue', foreground='black', font=('Segoe UI', 11))
style.configure('TOptionMenu', font=('Segoe UI', 10))

# Title Label
Label(root, text="Language Translator", font=("Segoe UI", 16, "bold"), bg="lightblue", fg="black").pack(pady=10)

# Input Text Frame
input_frame = Frame(root, bg="lightblue")
input_frame.pack(pady=5)
Label(input_frame, text="Enter Text:", bg="lightblue", fg="black", font=("Segoe UI", 11)).pack(anchor="w")
input_text = Text(input_frame, height=5, width=60, font=("Segoe UI", 10), bg="white", fg="black")
input_text.pack(pady=5)

# Language Selection Frame
lang_frame = Frame(root, bg="lightblue")
lang_frame.pack(pady=10)

Label(lang_frame, text="From:", font=("Segoe UI", 11), bg="lightblue", fg="black").grid(row=0, column=0, padx=5)
src_lang = StringVar(value="english")
src_menu = OptionMenu(lang_frame, src_lang, *languages)
src_menu.config(bg="white", fg="black", font=("Segoe UI", 10))
src_menu.grid(row=0, column=1, padx=5)

Label(lang_frame, text="To:", font=("Segoe UI", 11), bg="lightblue", fg="black").grid(row=0, column=2, padx=5)
dest_lang = StringVar(value="tamil")
dest_menu = OptionMenu(lang_frame, dest_lang, *languages)
dest_menu.config(bg="white", fg="black", font=("Segoe UI", 10))
dest_menu.grid(row=0, column=3, padx=5)

# Translate function
def translate():
    try:
        translated = translator.translate(
            input_text.get("1.0", END),
            src=src_lang.get(),
            dest=dest_lang.get()
        )
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {str(e)}")

# Translate Button
Button(root, text="Translate", command=translate, bg="gray", fg="black", font=("Segoe UI", 11)).pack(pady=15)

# Output Text Frame
output_frame = Frame(root, bg="lightblue")
output_frame.pack(pady=5)
Label(output_frame, text="Translated Text:", bg="lightblue", fg="black", font=("Segoe UI", 11)).pack(anchor="w")
output_text = Text(output_frame, height=5, width=60, font=("Segoe UI", 10), bg="white", fg="black")
output_text.pack(pady=5)

root.mainloop()
