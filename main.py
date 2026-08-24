import tkinter as tk
from tkfunctions import refresh_data, save_to_disk

def main():
    ### Main function to setup the GUI and bind the button to the function call
    root = tk.Tk()
    root.title("System Information")
    root.geometry("700x550")
    # Label of the App
    title_label = tk.Label(
        root,
        # this is the system information
        text="System Information",
        font=("Arial", 18)
    )
    title_label.pack(pady=10)
    #Text box
    text_box = tk.Text(
        root,
        width=80,
        height=25
    )

    text_box.pack(
        padx=10,
        pady=10,
        fill="both",
        expand=True
    )

    #Generate Stats Button (Below Text Box)

    refresh_button = tk.Button(
        root,
        text="Generate Stats",
        command=lambda: refresh_data(text_box)
    )
    refresh_button.pack(pady=5)

    #Save to Disk Button (Bottom)
    save_to_disk_button = tk.Button(
        root,
        text="Save to Disk",
        command=lambda: save_to_disk(text_box)
    )
    save_to_disk_button.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()