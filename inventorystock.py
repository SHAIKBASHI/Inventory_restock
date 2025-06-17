from datetime import datetime, timedelta

print("🛒 Inventory Restock Predictor\n")

# Step 1: Input sales data for the last 7 days
sales = []
for i in range(1, 8):
    units = int(input(f"Enter units sold on day {i}: "))
    sales.append(units)

# Step 2: Get current stock level
current_stock = int(input("\nEnter current stock level: "))

# Step 3: Calculate average daily sales
avg_sales = sum(sales) / len(sales)

# Step 4: Estimate how many days until stock runs out
if avg_sales == 0:
    print("\n🟢 No movement in stock. No need to restock now.")
else:
    days_left = current_stock / avg_sales
    run_out_date = datetime.today() + timedelta(days=days_left)

    print(f"\n📦 Average daily sales: {avg_sales:.2f} units")
    print(f"⏳ Estimated stock will run out in {days_left:.1f} days (~ {run_out_date.strftime('%d %b %Y')})")

    # Step 5: Suggest when to reorder (3 days before stock runs out)
    reorder_date = run_out_date - timedelta(days=3)
    print(f"🔁 Suggested reorder date: {reorder_date.strftime('%d %b %Y')}")

print("\n✅ Prediction complete. Stay stocked!")
