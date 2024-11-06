# Code with a bug
task_list = []

def add_task(task_description):
    """Adds a task to the to-do list."""
    if not task_description:
        return "Error: Task description cannot be empty."
    task_id = len(task_list) + 1  # Bug: ID depends on list length
    task_list.append({"id": task_id, "description": task_description, 
"status": "Pending"})
    return f"Task '{task_description}' added with ID {task_id}."

def remove_task(task_id):
    """Removes a task by its ID."""
    global task_list
    task_list = [task for task in task_list if task["id"] != task_id]
    return f"Task with ID {task_id} removed."
# 
Code 
with a bug
task_list = []

def add_task(task_description):
    """Adds a task to the to-do list."""
    if not task_description:
        return "Error: Task description cannot be empty."
    task_id = len(task_list) + 1  # Bug: ID depends on list length
    task_list.append({"id": task_id, "description": task_description, 
"status": "Pending"})
    return f"Task '{task_description}' added with ID {task_id}."

