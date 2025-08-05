import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

# --- Warehouse Setup ---
width, height = 10, 10
warehouse = np.zeros((height, width))
packing_station = (0, 0)
num_shelves = 50
shelves = random.sample([(x, y) for x in range(width) for y in range(height)], num_shelves)
for shelf in shelves:
    warehouse[shelf] = 1
num_items = 100
item_locations = {f"item_{i}": shelves[i // 2] for i in range(num_items)}
orders = [f"item_{random.randint(0, num_items - 1)}" for _ in range(10)]

# --- Distance Calculation ---
def manhattan_distance(point1, point2):
    """Calculate grid-based distance."""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def baseline_route(orders, item_locations, start_point):
    """Compute naive route."""
    route = [start_point]
    total_distance = 0
    current = start_point
    for item in orders:
        next_stop = item_locations[item]
        total_distance += manhattan_distance(current, next_stop)
        route.append(next_stop)
        current = next_stop
    total_distance += manhattan_distance(current, start_point)
    route.append(start_point)
    return route, total_distance

# --- Route Optimization ---
def greedy_route(orders, item_locations, start_point):
    """Optimize route by picking nearest item."""
    unvisited = orders.copy()
    current = start_point
    route = [start_point]
    total_distance = 0
    while unvisited:
        next_item = min(unvisited, key=lambda item: manhattan_distance(current, item_locations[item]))
        next_stop = item_locations[next_item]
        total_distance += manhattan_distance(current, next_stop)
        route.append(next_stop)
        current = next_stop
        unvisited.remove(next_item)
    total_distance += manhattan_distance(current, start_point)
    route.append(start_point)
    return route, total_distance

# --- Visualization ---
def plot_warehouse(warehouse, baseline_route, optimized_route):
    """Plot warehouse and routes."""
    plt.figure(figsize=(8, 8))
    plt.imshow(warehouse, cmap='Greys', origin='lower')
    plt.plot(*packing_station, 'ro', label='Packing Station')
    bx, by = zip(*baseline_route)
    plt.plot(bx, by, 'b--', label='Baseline Route')
    ox, oy = zip(*optimized_route)
    plt.plot(ox, oy, 'g-', label='Optimized Route')
    plt.legend()
    plt.title("Warehouse Route Optimization")
    plt.savefig("warehouse_plot.png")
    plt.show()

# --- Run Simulation ---
baseline_route, baseline_distance = baseline_route(orders, item_locations, packing_station)
optimized_route, optimized_distance = greedy_route(orders, item_locations, packing_station)
print(f"Baseline Distance: {baseline_distance} units")
print(f"Optimized Distance: {optimized_distance} units")
print(f"Improvement: {((baseline_distance - optimized_distance) / baseline_distance) * 100:.2f}%")

# Generate results table
data = {
    "Metric": ["Baseline Route", "Optimized Route", "Improvement"],
    "Distance (units)": [baseline_distance, optimized_distance, f"{((baseline_distance - optimized_distance) / baseline_distance) * 100:.2f}%"]
}
df = pd.DataFrame(data)
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.savefig("results_table.png")
plt.show()

plot_warehouse(warehouse, baseline_route, optimized_route)