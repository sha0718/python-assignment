import heapq

def max_tasks(tasks):
    """
    Determines the maximum number of tasks that can be completed before their deadlines.
    
    :param tasks: List of tasks, each with 'name', 'deadline', and 'duration'
    :return: List of task names that can be completed without missing deadlines
    """

    # Step 1: Sort tasks by their deadline (earliest first)
    tasks.sort(key=lambda x: x['deadline'])

    # Min-heap to track current tasks based on duration
    current_schedule = []
    total_time = 0

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']

        # Add task duration to total time
        total_time += duration
        # Push the task into the heap (we use negative duration for max-heap behavior)
        heapq.heappush(current_schedule, (-duration, task))

        # If total time exceeds deadline, remove the longest duration task
        if total_time > deadline:
            removed_duration, removed_task = heapq.heappop(current_schedule)
            total_time += removed_duration  # Subtract since removed_duration is negative

    # Extract task names from the heap
    selected_tasks = [task['name'] for _, task in current_schedule]

    return selected_tasks

# Example input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2}
]

# Run the scheduler
result = max_tasks(tasks)
print("Tasks that can be completed on time:", result)
