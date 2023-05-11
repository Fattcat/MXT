import tkinter as tk

def show_message():
    top = tk.Toplevel()
    top.title("Vyhľadávanie dokončené")
    top.geometry("200x200")
    msg = tk.Message(top, text="Hello " + search_var.get())
    msg.pack(expand=True)

def search():
    results_list.delete(0, tk.END)
    query = search_var.get().lower()
    for item in items:
        if query in item.lower():
            results_list.insert(tk.END, item)

root = tk.Tk()
root.title("Search Bar Example")

# Vytvorenie vstupného políčka (search bar) a tlačidla pre vyhľadávanie
search_var = tk.StringVar()
search_var.trace("w", lambda name, index, mode, sv=search_var: search())
search_entry = tk.Entry(root, textvariable=search_var)
search_entry.pack(padx=10, pady=10)
search_button = tk.Button(root, text="Vyhľadať", command=show_message)
search_button.pack(pady=10)

# Vytvorenie zoznamu výsledkov vyhľadávania
results_frame = tk.Frame(root)
results_frame.pack()
results_scrollbar = tk.Scrollbar(results_frame)
results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_list = tk.Listbox(results_frame, yscrollcommand=results_scrollbar.set)
results_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
results_scrollbar.config(command=results_list.yview)

# Zoznam položiek pre vyhľadávanie
items = ["LoL", "bab", "ale", "bob", "iba", "LoLbab", "alebobiba"]

root.mainloop()
