import tkinter as tk

# 1. SETUP & VARIABLES
root = tk.Tk()
root.title("Final Game Starter Kit")

money = 100
inventory = 0
score = 0

# 2. LOGIC FUNCTIONS
def update_ui():
    stats_label.config(text=f"Money: ${money} | Inventory: {inventory} | Score: {score}")

def buy_item():
    global money, inventory
    if money >= 10:
        money -= 10
        inventory += 1
        status_label.config(text="Bought an item!", fg="green")
        update_ui()
    else:
        status_label.config(text="Not enough money!", fg="red")

def sell_item():
    global money, inventory
    if inventory > 0:
        money += 10
        inventory -= 1
        status_label.config(text="Sold an item!", fg="green")
        update_ui()

# 3. MOVEMENT LOGIC (For Platformers/Action)
def move_player(event):
    key = event.keysym
    if key == "Up":
        canvas.move(player, 0, -10)
    elif key == "Down":
        canvas.move(player, 0, 10)
    elif key == "Left":
        canvas.move(player, -10, 0)
    elif key == "Right":
        canvas.move(player, 10, 0)
        
        
    # Get the current position of the player
    p_pos = canvas.coords(player) 
    
    # Look for items overlapping the player's area
    overlapping = canvas.find_overlapping(p_pos[0], p_pos[1], p_pos[2], p_pos[3])
    
    # If the 'goal' ID is in that list, something happened!
    if goal in overlapping:
        status_label.config(text="YOU WIN! You touched the goal!", fg="orange")
        canvas.itemconfig(goal, fill="green") # Change color when touched
        
    

# 4. GUI LAYOUT
stats_label = tk.Label(root, text=f"Money: ${money} | Inventory: {inventory} | Score: {score}", font=("Arial", 12))
stats_label.pack(pady=5)

canvas = tk.Canvas(root, width=400, height=300, bg="lightblue")
canvas.pack()

# Create a player (Blue) and a Goal (Gold)
player = canvas.create_rectangle(180, 130, 220, 170, fill="blue")
goal = canvas.create_oval(300, 50, 330, 80, fill="gold")

status_label = tk.Label(root, text="Use Arrows to move. Use Buttons to trade.", fg="gray")
status_label.pack()

# 5. BUTTONS & BINDINGS
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Buy Item ($10)", command=buy_item).pack(side="left", padx=5)
tk.Button(btn_frame, text="Sell Item ($10)", command=sell_item).pack(side="left", padx=5)

# Connects keyboard to the movement function
root.bind("<Key>", move_player)

root.mainloop()
