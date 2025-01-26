import random

NUM_DAYS = 2000
PURCHASE_QTY = 70  
PURCHASE_COST = 0.33  
SELLING_PRICE = 0.50  
SALVAGE_VALUE = 0.05  
LOST_PROFIT = 0.17  

newsday_types = ['Good', 'Fair', 'Poor']
newsday_probs = [0.35, 0.45, 0.20]

demand_dist = {
    'Good': [(40, 0.03), (50, 0.05), (60, 0.15), (70, 0.20), (80, 0.35), (90, 0.15), (100, 0.07)],
    'Fair': [(40, 0.10), (50, 0.18), (60, 0.40), (70, 0.20), (80, 0.08), (90, 0.04), (100, 0.00)],
    'Poor': [(40, 0.44), (50, 0.22), (60, 0.16), (70, 0.12), (80, 0.06), (90, 0.00), (100, 0.00)]
}

demand_random_digits = {
    'Good': [(40, range(1, 4)), (50, range(4, 9)), (60, range(9, 24)), (70, range(24, 44)),
             (80, range(44, 79)), (90, range(79, 94)), (100, range(94, 101))],
    'Fair': [(40, range(1, 11)), (50, range(11, 29)), (60, range(29, 69)), (70, range(69, 89)),
             (80, range(89, 97)), (90, range(97, 101)), (100, range(101, 101))],
    'Poor': [(40, range(1, 45)), (50, range(45, 67)), (60, range(67, 83)), (70, range(83, 95)),
             (80, range(95, 101)), (90, range(101, 101)), (100, range(101, 101))]
}

def get_newsday_type():
    rand_num = random.randint(1, 100)
    if rand_num <= 35:
        return 'Good'
    elif rand_num <= 80:
        return 'Fair'
    else:
        return 'Poor'

def get_demand(newsday_type):
    rand_num = random.randint(1, 100)
    for demand, rand_range in demand_random_digits[newsday_type]:
        if rand_num in rand_range:
            return demand
    return 0

simulation_table = []

total_revenue = 0
total_lost_profit = 0
total_salvage = 0
total_daily_profit = 0

for day in range(1, NUM_DAYS + 1):
    
    newsday_type = get_newsday_type()
    demand = get_demand(newsday_type)
    
    sold = min(demand, PURCHASE_QTY)
    revenue = sold * SELLING_PRICE
    
    lost_profit = max(0, demand - PURCHASE_QTY) * LOST_PROFIT
    
    unsold = max(0, PURCHASE_QTY - demand)
    salvage = unsold * SALVAGE_VALUE
    
    daily_profit = revenue - (PURCHASE_QTY * PURCHASE_COST) - lost_profit + salvage
    
    total_revenue += revenue
    total_lost_profit += lost_profit
    total_salvage += salvage
    total_daily_profit += daily_profit
    
    simulation_table.append([
        day, newsday_type, demand, revenue, lost_profit, salvage, daily_profit
    ])

print("Day | Newsday Type | Demand | Revenue from Sales | Lost Profit from Excess Demand | Salvage from Sale of Scrap | Daily Profit")
for row in simulation_table:
    print(f"{row[0]} | {row[1]} | {row[2]} | ${row[3]:.2f} | ${row[4]:.2f} | ${row[5]:.2f} | ${row[6]:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")
print(f"Total Lost Profit: ${total_lost_profit:.2f}")
print(f"Total Salvage: ${total_salvage:.2f}")
print(f"Total Daily Profit: ${total_daily_profit:.2f}")