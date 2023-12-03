import tkinter as tk
import subprocess

root = tk.Tk()
input_data = "hi"
result = subprocess.run(["test2.exe", input_data],
                        capture_output=True, text=True, check=True)
output_text = result.stdout.strip()  # Get and strip the output
txt = tk.Text(root, text=output_text)
txt.pack()
root.mainloop()
