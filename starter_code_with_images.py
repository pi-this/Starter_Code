import tkinter as tk
from PIL import Image, ImageTk 

# 1. SETUP & VARIABLES
root = tk.Tk()
root.title("Final Game Starter Kit")

money = 100
inventory = 0
score = 0

# --- NEW: LOAD IMAGES ---
# Load and resize the player image
player_img_raw = Image.open("cat.png").resize((40, 40))
player_img = ImageTk.PhotoImage(player_img_raw)

# Load and resize the goal image
goal_img_raw = Image.open("star.png").resize((30, 30))
goal_img = ImageTk.PhotoImage(goal_img_raw)

cart_img_raw = Image.open("cart.png").resize((30, 30))
cart_img = ImageTk.PhotoImage(cart_img_raw)

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

# 3. MOVEMENT LOGIC
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
        
    p_pos = canvas.bbox(player) # Use bbox for images to get coordinates
    overlapping = canvas.find_overlapping(p_pos[0], p_pos[1], p_pos[2], p_pos[3])
    
    if goal in overlapping:
        status_label.config(text="YOU WIN! You reached the goal!", fg="orange")

# 4. GUI LAYOUT
stats_label = tk.Label(root, text=f"Money: ${money} | Inventory: {inventory} | Score: {score}", font=("Arial", 12))
stats_label.pack(pady=5)

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# --- CHANGED: Use create_image instead of shapes ---
# anchor="nw" makes the (x, y) point the Top-Left corner (similar to rectangles)
cart = canvas.create_image(200, 100, image=cart_img, anchor="nw")
goal = canvas.create_image(300, 50, image=goal_img, anchor="nw")
player = canvas.create_image(180, 130, image=player_img, anchor="nw")


status_label = tk.Label(root, text="Use Arrows to move. Use Buttons to trade.", fg="gray")
status_label.pack()

# 5. BUTTONS & BINDINGS
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Buy Item ($10)", command=buy_item).pack(side="left", padx=5)
tk.Button(btn_frame, text="Sell Item ($10)", command=sell_item).pack(side="left", padx=5)

root.bind("<Key>", move_player)
root.mainloop()

