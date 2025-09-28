import turtle
from menu import MENU_PRICES

# --- Setup drawing turtles ---
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(0)
writer.penup()

# --- Order storage ---
order_items = []  # list of (name, price) tuples
buttons = []  # button areas and actions


def draw_box(x, y, w, h, label, action=None):
    """Draw a rectangular button/box with label and store its action."""
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(0)
    drawer.color("black", "chocolate")
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(w)
        drawer.right(90)
        drawer.forward(h)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

    # Write label
    drawer.goto(x + w / 2, y - h / 2 - 8)
    drawer.write(label, align="center", font=("Arial", 14, "bold"))

    # Store button area
    if action:
        buttons.append({"x1": x, "y1": y, "x2": x + w, "y2": y - h, "action": action})


def check_click(x, y):
    """Check if a click falls inside a button and run its action."""
    for btn in buttons:
        if btn["x1"] <= x <= btn["x2"] and btn["y2"] <= y <= btn["y1"]:
            btn["action"]()


def add_item(item_name):
    """Add an item with price to the order list."""
    price = MENU_PRICES.get(item_name, 0.00)
    order_items.append((item_name, price))
    update_order_summary()


def update_order_summary():
    """Refresh the order summary box with current items."""
    writer.clear()
    start_y = -180
    writer.goto(-280, start_y)
    writer.write("Your Order:", font=("Arial", 14, "bold"))
    y_offset = 25
    total = 0
    for i, (item, price) in enumerate(order_items, start=1):
        writer.goto(-280, start_y - i * y_offset)
        writer.write(f"{i}. {item} - ${price:.2f}", font=("Arial", 12, "normal"))
        total += price

    # Show total at bottom
    writer.goto(-280, start_y - (len(order_items) + 2) * y_offset)
    writer.write(f"Total: ${total:.2f}", font=("Arial", 14, "bold"))


def clear_order():
    """Reset order list."""
    order_items.clear()
    update_order_summary()