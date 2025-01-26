# 2-Server Simulation

## Overview

This Python simulation models a call center with two agents (Able and Baker) to analyze performance metrics using discrete event simulation techniques.

## Features

- Simulate call center operations over a specified time period
- Model call arrivals using exponential distribution
- Track agent utilization and customer waiting times
- Generate key performance indicators


## Simulation Parameters

- **Simulation Time**: 8 hours (480 minutes)
- **Call Arrival Rate**: 10 calls per hour
- **Agent Service Rates**:
  - Able: 12 calls per hour
  - Baker: 8.57 calls per hour

## Key Metrics Calculated

1. Total calls received
2. Average waiting time
3. Average queue length
4. Agent utilization percentages

## Simulation Methodology

### Event Types
- Call Arrival
- Call Departure (for Able)
- Call Departure (for Baker)

### Modeling Approach
- Uses discrete event simulation
- Exponential distribution for service times
- Priority queue for event scheduling

## Running the Simulation

```bash
python3 python-impl.py
```

## Sample Output
```
Simulation Table for Call-Center Example
Caller | Interarrival Time | Arrival Time | Able Available | Baker Available | Server Chosen | Service Time | Service Begins | Completion Time | Caller Delay | Time in System
[1, 2, 2, True, False, 'Able', 2, 2, 4, 0, 2]
[2, 3, 5, True, False, 'Able', 4, 5, 9, 0, 4]
[3, 2, 7, True, True, 'Baker', 6, 7, 13, 0, 6]
.......

Total calls: 480
Average waiting time: 0.75 minutes
Average queue length: 0.50
Able utilization: 85.50%
Baker utilization: 70.25%
```

## Performance Insights

The simulation helps analyze:
- Queue management efficiency
- Agent workload distribution
- Customer wait time expectations

## Customization

Modify simulation parameters in the script to:
- Adjust arrival rates
- Change simulation duration
- Experiment with different service rates

## Limitations

- Assumes exponential service times
- Uses simplified call center model
- Stochastic nature means results vary between runs
