def update_task(task_id, new_description=None, new_status=None):
    """Updates the task's description or status."""
    for task in task_list:
        if task["id"] == task_id:
            if new_description:
                task["description"] = new_description

