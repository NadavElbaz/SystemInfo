from systemutils import get_system_info
from pathlib import Path
import tkinter as tk

def refresh_data(text_box):
    ### Function to fetch system info and populate the GUI with the data
    info_lines = ""

    for key, value in get_system_info().items():
        info_lines += f"{key}: {value}\n"

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, info_lines)

def save_to_disk(varibale1):
    content = varibale1.get("1.0", tk.END)
    folder_path = Path("/Users/nadavelbaz/PycharmProjects/Nadav Project")
    file_path = folder_path/"test.txt"
    file_path.write_text(content, encoding="utf-8")

    file_path2 = folder_path / "test2.txt"
    file_path2.write_text(content, encoding="utf-8")
