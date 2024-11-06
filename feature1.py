# Code without a bug
task_list = []
task_counter = 1  # Initialize a unique task counter

def add_task(task_description):
    """Adds a task to the to-do list."""
    global task_counter
    if not task_description:
        return "Error: Task description cannot be empty."
    task_id = task_counter  # Unique task ID based on counter
    task_list.append({"id": task_id, "description": task_description, "status": "Pending"})
    task_counter += 1  # Increment counter for next task
    return f"Task '{task_description}' added with ID {task_id}."

def remove_task(task_id):
    """Removes a task by its ID."""
    global task_list
    task_list = [task for task in task_list if task["id"] != task_id]
    return f"Task with ID {task_id} removed."

