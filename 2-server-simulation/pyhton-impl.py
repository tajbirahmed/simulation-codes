import random
import heapq

# Simulation Configuration
# Define the total simulation time in minutes (8 hours = 480 minutes)
SIM_TIME = 480  

# Call Center Parameters
# Arrival rate: Average number of calls received per hour
ARRIVAL_RATE = 10  

# Service rates for two call center agents
# Able can handle more calls per hour compared to Baker
SERVICE_RATE_ABLE = 12    # Able handles 12 calls per hour
SERVICE_RATE_BAKER = 8.57 # Baker handles 8.57 calls per hour

# Convert rates from per-hour to per-minute for precise simulation
# This allows for more granular event scheduling
ARRIVAL_RATE = ARRIVAL_RATE / 60
SERVICE_RATE_ABLE = SERVICE_RATE_ABLE / 60
SERVICE_RATE_BAKER = SERVICE_RATE_BAKER / 60

# Event Type Constants
# Define unique identifiers for different event types in the simulation
ARRIVAL = 1       # New call arriving at the call center
DEPARTURE_ABLE = 2 # Call completed by Able
DEPARTURE_BAKER = 3 # Call completed by Baker

# Initialize Simulation State Variables
clock = 0         # Tracks the current simulation time
able_busy = False # Tracks if Able is currently serving a call
baker_busy = False # Tracks if Baker is currently serving a call
queue = []        # Holds calls waiting to be served
heap = []         # Priority queue to manage event scheduling
heapq.heapify(heap)

# Performance Tracking Variables
total_calls = 0         # Total number of calls received
total_waiting_time = 0  # Cumulative waiting time for all calls
total_queue_length = 0  # Tracks total queue length over time
able_utilization = 0    # Tracks Able's service time
baker_utilization = 0   # Tracks Baker's service time

# Generate Random Service Times
# Uses exponential distribution to model real-world call service times
# Exponential distribution mimics variability in call duration
def expovariate(rate):
    """
    Generate a random service time using exponential distribution.
    
    Args:
        rate (float): Rate parameter for exponential distribution
    
    Returns:
        float: Randomly generated service time
    """
    return random.expovariate(rate)

# Schedule the first call arrival
# Determines when the first call will arrive using exponential distribution
first_arrival = expovariate(ARRIVAL_RATE)
heapq.heappush(heap, (first_arrival, ARRIVAL))

# Main Simulation Loop
# Processes events chronologically until simulation time is exhausted
while clock < SIM_TIME:
    # Extract the next event with the earliest timestamp
    current_event = heapq.heappop(heap)
    clock = current_event[0]  # Update simulation clock
    event_type = current_event[1]

    # Handle Call Arrival Event
    if event_type == ARRIVAL:
        # Schedule next call arrival
        next_arrival = clock + expovariate(ARRIVAL_RATE)
        heapq.heappush(heap, (next_arrival, ARRIVAL))
        
        total_calls += 1  # Increment total calls received

        # Check if Able is available to take the call
        if not able_busy:
            able_busy = True
            service_time = expovariate(SERVICE_RATE_ABLE)
            heapq.heappush(heap, (clock + service_time, DEPARTURE_ABLE))
            able_utilization += service_time
        
        # If Able is busy, check if Baker is available
        elif not baker_busy:
            baker_busy = True
            service_time = expovariate(SERVICE_RATE_BAKER)
            heapq.heappush(heap, (clock + service_time, DEPARTURE_BAKER))
            baker_utilization += service_time
        
        # If both agents are busy, add call to waiting queue
        else:
            queue.append(clock)
            total_queue_length += 1

    # Handle Departure Event for Able
    elif event_type == DEPARTURE_ABLE:
        able_busy = False

        # If calls are waiting in queue, assign next call to Able
        if queue:
            call_arrival_time = queue.pop(0)
            waiting_time = clock - call_arrival_time
            total_waiting_time += waiting_time
            
            able_busy = True
            service_time = expovariate(SERVICE_RATE_ABLE)
            heapq.heappush(heap, (clock + service_time, DEPARTURE_ABLE))
            able_utilization += service_time

    # Handle Departure Event for Baker
    elif event_type == DEPARTURE_BAKER:
        baker_busy = False

        # If calls are waiting in queue, assign next call to Baker
        if queue:
            call_arrival_time = queue.pop(0)
            waiting_time = clock - call_arrival_time
            total_waiting_time += waiting_time
            
            baker_busy = True
            service_time = expovariate(SERVICE_RATE_BAKER)
            heapq.heappush(heap, (clock + service_time, DEPARTURE_BAKER))
            baker_utilization += service_time

# Calculate Performance Metrics
# Compute key performance indicators for the call center
average_waiting_time = total_waiting_time / total_calls
average_queue_length = total_queue_length / total_calls
able_utilization = able_utilization / SIM_TIME
baker_utilization = baker_utilization / SIM_TIME

# Output Simulation Results
# Display key metrics to analyze call center performance
print(f"Total calls: {total_calls}")
print(f"Average waiting time: {average_waiting_time:.2f} minutes")
print(f"Average queue length: {average_queue_length:.2f}")
print(f"Able utilization: {able_utilization:.2%}")
print(f"Baker utilization: {baker_utilization:.2%}")