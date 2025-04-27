import tkinter as tk
import subprocess

def open_sand_simulation():
    subprocess.Popen(["python3", "sand.py"])

def open_game_of_life():
    subprocess.Popen(["python3", "game-of-life.py"])

root = tk.Tk()
root.title("Simulation Selector")
root.geometry("300x200")

label = tk.Label(root, text="Select a Simulation", font=("Arial", 16))
label.pack(pady=20)

sand_button = tk.Button(root, text="Sand Falling Simulation", command=open_sand_simulation, width=25)
sand_button.pack(pady=10)

life_button = tk.Button(root, text="Conway's Game of Life", command=open_game_of_life, width=25)
life_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()