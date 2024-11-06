# feature1.py with hotfixes applied
task_list = []

def add_task(task_description):
    """Adds a task to the to-do list with validation for description."""
    # Hotfix for critical bug: Ensure task_description is a non-empty string
    if not task_description or not isinstance(task_description, str):
        return "Error: Task description must be a non-empty string."
    task_id = len(task_list) + 1
    task_list.append({"id": task_id, "description": task_description, "status": "Pending"})
    return f"Task '{task_description}' added with ID {task_id}."

def remove_task(task_id):
    """Removes a task by its ID."""
    global task_list
    # Hotfix for bug Y: Verify task_id exists before removing
    task_exists = any(task["id"] == task_id for task in task_list)
    if not task_exists:
        return f"Error: Task with ID {task_id} not found."
    task_list = [task for task in task_list if task["id"] != task_id]
    return f"Task with ID {task_id} removed."
