from uuid import UUID
from src.todo.storage import InMemoryTaskStorage
from src.todo.service import TodoService

class TodoManager:
    """Wrapper class for backward compatibility with main.py"""
    def __init__(self):
        self.storage = InMemoryTaskStorage()
        self.service = TodoService(self.storage)

    def add_task(self, title: str, description: str = None):
        return self.service.add_task(title, description or "")

    def get_all_tasks(self):
        return self.service.list_tasks()

    def get_task_by_id(self, task_id):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.storage.get(uuid_id)
        except (ValueError, TypeError):
            return None

    def update_task(self, task_id, title: str = None, description: str = None, completed: bool = None):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.service.update_task(uuid_id, title, description, completed)
        except (ValueError, TypeError):
            return None

    def delete_task(self, task_id):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.service.delete_task(uuid_id)
        except (ValueError, TypeError):
            return False

    def toggle_task_status(self, task_id):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.service.toggle_task(uuid_id)
        except (ValueError, TypeError):
            return None

    def complete_task(self, task_id):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.service.complete_task(uuid_id)
        except (ValueError, TypeError):
            return None

    def incomplete_task(self, task_id):
        try:
            uuid_id = task_id if isinstance(task_id, UUID) else UUID(str(task_id))
            return self.service.incomplete_task(uuid_id)
        except (ValueError, TypeError):
            return None
