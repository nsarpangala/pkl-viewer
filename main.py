import tkinter as tk
from tkinter import filedialog, messagebox
import pickle
import pprint

def load_pkl_file(text_box):
    file_path = filedialog.askopenfilename(
        title="Open .pkl file",
        filetypes=[("Pickle files", "*.pkl"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "rb") as f:
                data = pickle.load(f)
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, pprint.pformat(data))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load .pkl file:\n{e}")

def run_gui():
    root = tk.Tk()
    root.title("Pickle File Viewer")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    text_box = tk.Text(root, wrap=tk.NONE, height=30, width=100)
    text_box.pack(padx=10, pady=10)

    load_button = tk.Button(frame, text="Open Pickle File", command=lambda: load_pkl_file(text_box))
    load_button.pack()

    root.mainloop()
