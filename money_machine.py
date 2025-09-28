
def pay_now(screen):
    writer.goto(-280, -300)
    if order_items:
        total = sum(price for _, price in order_items)
        writer.write(f"Payment processed: ${total:.2f}", font=("Arial", 14, "bold"))
        order_items.clear()
        screen.ontimer(update_order_summary, 2000)
    else:
        writer.write("No items in order!", font=("Arial", 14, "bold"))