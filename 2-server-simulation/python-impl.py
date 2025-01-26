import random

# Simulation Configuration
SIM_TIME = 480  # Total simulation time in minutes
NUM_CALLS = 100  # Total number of calls to simulate in the scenario

# Probability Distributions for Call Center Simulation
# Each distribution is structured as: (service_time, probability, cumulative_probability, random_number_range)
# Allows for non-uniform service times and interarrival intervals

# Interarrival Time Distribution
interarrival_dist = [
    (1, 0.25, 0.25, range(1, 26)),    
    (2, 0.40, 0.65, range(26, 66)),   
    (3, 0.20, 0.85, range(66, 86)),   
    (4, 0.15, 1.00, range(86, 101))   
]

# Service Time Distribution for Able
able_dist = [
    (2, 0.30, 0.30, range(1, 31)),    
    (3, 0.28, 0.58, range(31, 59)),   
    (4, 0.25, 0.83, range(59, 84)),   
    (5, 0.17, 1.00, range(84, 101))   
]

# Service Time Distribution for Baker
baker_dist = [
    (3, 0.35, 0.35, range(1, 36)),    
    (4, 0.25, 0.60, range(36, 61)),   
    (5, 0.20, 0.80, range(61, 81)),   
    (6, 0.20, 1.00, range(81, 101))   
]

# Random Variate Generation Function
def generate_random_variate(distribution):
    """
    Generates a random service time based on the provided probability distribution.
    
    Args:
        distribution (list): Probability distribution of service times
    
    Returns:
        int: Randomly selected service time
    """
    rand_num = random.randint(1, 100)
    for time, prob, cum_prob, rand_range in distribution:
        if rand_num in rand_range:
            return time
    return 0

# State Variables
clock = 0             
able_busy = False     
baker_busy = False    
queue = []            
simulation_table = []  


total_calls = 0        
total_waiting_time = 0 
total_queue_length = 0 
able_utilization = 0   
baker_utilization = 0  

# Initial Call Arrival Schedule
# Determine first call's arrival time
interarrival_time = generate_random_variate(interarrival_dist)
arrival_time = clock + interarrival_time

# Main Simulation Loop
while total_calls < NUM_CALLS:
    # Handle Call Arrivals
    if arrival_time <= clock:
        total_calls += 1


        # Prioritize Able, then Baker if Able is busy
        if not able_busy:
            able_busy = True
            service_time = generate_random_variate(able_dist)
            completion_time = clock + service_time
            able_utilization += service_time
            server_chosen = 'Able'
        elif not baker_busy:
            baker_busy = True
            service_time = generate_random_variate(baker_dist)
            completion_time = clock + service_time
            baker_utilization += service_time
            server_chosen = 'Baker'
        else:
            # If both agents are busy, add to waiting queue
            queue.append((arrival_time, total_calls))
            total_queue_length += 1
            server_chosen = 'None'

        # Record Simulation Event
        if server_chosen != 'None':
            simulation_table.append([
                total_calls, interarrival_time, arrival_time, able_busy, baker_busy,
                server_chosen, service_time, clock, completion_time, 0, service_time
            ])
        else:
            simulation_table.append([
                total_calls, interarrival_time, arrival_time, able_busy, baker_busy,
                server_chosen, 0, 0, 0, 0, 0
            ])

        # Schedule Next Call Arrival
        interarrival_time = generate_random_variate(interarrival_dist)
        arrival_time = clock + interarrival_time

    # Handle Call Departures -- Able
    if able_busy:
        for event in simulation_table:
            if event[8] == clock and event[5] == 'Able':
                able_busy = False
                # Waiting Queue
                if queue:
                    call_arrival_time, call_number = queue.pop(0)
                    waiting_time = clock - call_arrival_time
                    total_waiting_time += waiting_time
                    able_busy = True
                    service_time = generate_random_variate(able_dist)
                    completion_time = clock + service_time
                    able_utilization += service_time
                    simulation_table[call_number - 1] = [
                        call_number, interarrival_time, call_arrival_time, able_busy, baker_busy,
                        'Able', service_time, clock, completion_time, waiting_time, service_time
                    ]

    # Handle Call Departures -- Baker
    if baker_busy:
        for event in simulation_table:
            if event[8] == clock and event[5] == 'Baker':
                baker_busy = False
                # Waiting Queue
                if queue:
                    call_arrival_time, call_number = queue.pop(0)
                    waiting_time = clock - call_arrival_time
                    total_waiting_time += waiting_time
                    baker_busy = True
                    service_time = generate_random_variate(baker_dist)
                    completion_time = clock + service_time
                    baker_utilization += service_time
                    simulation_table[call_number - 1] = [
                        call_number, interarrival_time, call_arrival_time, able_busy, baker_busy,
                        'Baker', service_time, clock, completion_time, waiting_time, service_time
                    ]

    
    clock += 1

average_waiting_time = total_waiting_time / total_calls
average_queue_length = total_queue_length / total_calls
able_utilization = able_utilization / clock
baker_utilization = baker_utilization / clock


print("Simulation Table for 2 - Server")
print("Caller | Interarrival Time | Arrival Time | Able Available | Baker Available | Server Chosen | Service Time | Service Begins | Completion Time | Caller Delay | Time in System")
for event in simulation_table:
    print(event)

# Print Performance Metrics
print(f"\nTotal calls: {total_calls}")
print(f"Average waiting time: {average_waiting_time:.2f} minutes")
print(f"Average queue length: {average_queue_length:.2f}")
print(f"Able utilization: {able_utilization:.2%}")
print(f"Baker utilization: {baker_utilization:.2%}")