# Data Visualizer & Analyzer – Offline, No API Required

import tkinter as tk
from tkinter import filedialog, scrolledtext
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# === GUI Setup ===
root = tk.Tk()
root.title("📊 Smart Data Analyzer")
root.geometry("900x600")
root.configure(bg="#1e1e2f")

header = tk.Label(root, text="Smart Data Visualizer & Analyzer", font=("Helvetica", 18, "bold"), bg="#1e1e2f", fg="white")
header.pack(pady=10)

desc = tk.Label(root, text="Load a CSV file to view stats, visualize data, and detect outliers.", font=("Helvetica", 12), bg="#1e1e2f", fg="lightgray")
desc.pack()

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 10), bg="#2e2e3e", fg="white",
                                       insertbackground="white", height=18)
output_box.pack(expand=True, fill='both', padx=20, pady=10)

# === File Analysis ===
def analyze_csv():
    output_box.delete("1.0", tk.END)
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        output_box.insert(tk.END, f"Loaded file: {os.path.basename(file_path)}\n\n")
        output_box.insert(tk.END, "=== Dataset Summary ===\n")
        output_box.insert(tk.END, df.describe().to_string() + "\n\n")

        output_box.insert(tk.END, "=== Null Values ===\n")
        output_box.insert(tk.END, df.isnull().sum().to_string() + "\n\n")

        output_box.insert(tk.END, "=== Correlation Heatmap ===\n")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        output_box.insert(tk.END, f"[ERROR] {str(e)}")

# === Button ===
btn = tk.Button(root, text="📂 Load CSV File", command=analyze_csv,
                font=("Arial", 12), bg="#2196F3", fg="white", padx=20, pady=10, bd=0, relief="ridge")
btn.pack(pady=10)

root.mainloop()
