# main.py
import turtle
from coffee_maker import draw_box, check_click, add_item, clear_order, update_order_summary


# --- Setup screen ---
screen = turtle.Screen()
screen.title("Coffee Machine")
screen.setup(width=800, height=600)
screen.bgcolor("white")


def draw_coffee_machine_ui():
    # Title
    draw_box(-300, 250, 600, 60, "Welcome to our Coffee Shop!")

    # Menu buttons
    draw_box(-300, 150, 180, 50, "Espresso", lambda: add_item("Espresso"))
    draw_box(-90, 150, 180, 50, "Latte", lambda: add_item("Latte"))
    draw_box(120, 150, 180, 50, "Cappuccino", lambda: add_item("Cappuccino"))

    # Size buttons
    draw_box(-300, 60, 120, 40, "Small", lambda: add_item("Small Size"))
    draw_box(-160, 60, 120, 40, "Medium", lambda: add_item("Medium Size"))
    draw_box(-20, 60, 120, 40, "Large", lambda: add_item("Large Size"))

    # Add-ons
    draw_box(120, 60, 180, 40, "Add-ons", lambda: add_item("Add-ons"))


    # Order summary box
    draw_box(-300, -50, 600, 400, "Order Summary")
    update_order_summary()


# --- Run ---
draw_coffee_machine_ui()
screen.onclick(check_click)
screen.mainloop()