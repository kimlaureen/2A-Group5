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

