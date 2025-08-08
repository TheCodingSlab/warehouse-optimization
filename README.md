# AI-Driven Warehouse Route Optimization
## Overview
A Python-based simulation to optimize order-picking routes in a 10x10 factory warehouse with randomized shelves in structured storage zones, reducing travel distance by [Your %]% using a greedy algorithm.

## Problem
Minimize travel distance for pickers fulfilling 10 random orders in a warehouse with 50 shelves and 100 items.

## Warehouse Specifications
- 10x10 grid (100 cells): 50 shelves (black), aisles (white) in columns 3, 7 and rows 3, 7, 1 packing station (red dot at (0,0)).
- Shelves randomly placed in storage zones, labeled S1-S50, each holding ~2 items.
- Aisles form cross-shaped navigable paths; no enclosed rooms, open grid layout.
- Randomized shelves within zones simulate real-world variability.

## Factory Layout Efficiency
- Structured aisles reduce congestion and enable efficient Manhattan distance routing.
- Randomized shelves in zones balance flexibility and organization for varying orders.

## Solution
- Modeled warehouse using NumPy.
- Implemented greedy algorithm to select nearest items.
- Visualized routes with Matplotlib (black: shelves, white: aisles).

## Results
| Metric            | Distance (units) |
|-------------------|------------------|
| Baseline Route    | [Your Baseline]  |
| Optimized Route   | [Your Optimized] |
| Improvement       | [Your %]         |

![Warehouse Routes](<img width="600" height="200" alt="Figure_1" src="https://github.com/user-attachments/assets/5f94b825-9dc1-4333-a42c-5ef4cbaf4522" />)

![Results Table](<img width="1536" height="754" alt="Figure_2" src="https://github.com/user-attachments/assets/8745d10e-e5fb-437f-92eb-8ca8f45fea20" />)

![Greedy Algorithm](code_snippet.png)

## Tools
- Python, NumPy, Matplotlib, Pandas

## Installation
```bash
pip install numpy matplotlib pandas
python warehouse_opt.py
