import tkinter as tk
root = tk.Tk()
root.geometry("800x500")
# : top
top_frame = tk.Frame(root, bg="lightblue", height=50)
top_frame.pack(fill=tk.X)

# :right
right_frame = tk.Frame(root, bg="lightgreen", width=200)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)
button = tk.Button(top_frame, text="Click Me!")
button.pack(pady=10)

# middle
middle_frame = tk.Frame(root, bg="lightcoral")
middle_frame.pack(fill=tk.BOTH, expand=True)  # Fill remaining space

root.mainloop()


