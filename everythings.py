import os
import tkinter as tk
from tkinter import filedialog

def search_files(directory, query):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                found_files.append(os.path.join(root, file))
    return found_files

def search_button_click():
    directory = directory_entry.get()
    query = query_entry.get()
    
    if directory and query:
        found_files = search_files(directory, query)
        
        if found_files:
            result_text.delete(1.0, tk.END)
            for file in found_files:
                result_text.insert(tk.END, file + "\n")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No files found matching the query.")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter both directory and query.")

def browse_button_click():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

# Create main window
root = tk.Tk()
root.title("File Search Tool")

# Directory input
directory_frame = tk.Frame(root)
directory_frame.pack(pady=5)
directory_label = tk.Label(directory_frame, text="Directory:")
directory_label.pack(side=tk.LEFT)
directory_entry = tk.Entry(directory_frame, width=50)
directory_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(directory_frame, text="Browse", command=browse_button_click)
browse_button.pack(side=tk.LEFT)

# Query input
query_frame = tk.Frame(root)
query_frame.pack(pady=5)
query_label = tk.Label(query_frame, text="Search Query:")
query_label.pack(side=tk.LEFT)
query_entry = tk.Entry(query_frame, width=50)
query_entry.pack(side=tk.LEFT, padx=5)

# Search button
search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack(pady=5)

# Result display
result_text = tk.Text(root, height=15, width=70)
result_text.pack(pady=5)

# Run the main event loop
root.mainloop()