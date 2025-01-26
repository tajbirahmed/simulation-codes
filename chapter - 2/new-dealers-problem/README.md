# News Dealer's Problem Simulation

This Python script simulates the News Dealer's Problem, a classic inventory management problem. The goal is to determine the optimal number of newspapers a newsstand should purchase daily to maximize profit. The simulation considers different types of newsdays (Good, Fair, Poor) and their respective demand distributions.

## Problem Description

A newsstand buys newspapers for 33 cents each and sells them for 50 cents each. Unsold newspapers are sold as scrap for 5 cents each. Newspapers can only be purchased in bundles of 10. The newsstand experiences three types of newsdays with the following probabilities:

- **Good**: 35%
- **Fair**: 45%
- **Poor**: 20%

The demand for newspapers varies depending on the type of newsday. The simulation runs for 20 days and calculates the daily profit, revenue, lost profit from excess demand, and salvage from unsold newspapers.

## Code Overview

The Python script performs the following steps:

1. **Initialization**: Sets up parameters such as the number of days to simulate, purchase quantity, costs, and selling prices.
2. **Demand Distributions**: Defines the demand distributions for each type of newsday and their corresponding random digit assignments.
3. **Simulation**: Simulates the purchase and sale of newspapers over 20 days, considering the type of newsday and demand.
4. **Profit Calculation**: Calculates daily profit, revenue, lost profit, and salvage for each day.
5. **Output**: Generates a simulation table and totals for revenue, lost profit, salvage, and daily profit.

## How to Run the Code

1. Ensure you have Python installed on your system.
2. Clone this repository or download the Python script.
3. Run the script using the following command:

   ```bash
   python python-impl.py