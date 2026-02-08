from uuid import UUID
from datetime import datetime
from src.todo.models import Task
from src.todo.storage import InMemoryTaskStorage

class TodoService:
    def __init__(self, storage: InMemoryTaskStorage):
        self.storage = storage

    def add_task(self, title: str, description: str) -> Task:
        task = Task(title=title, description=description)
        self.storage.add(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self.storage.get_all()

    def update_task(self, task_id: UUID, title: str = None, description: str = None, completed: bool = None) -> Task | None:
        task = self.storage.get(task_id)
        if not task:
            return None
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        task.updated_at = datetime.utcnow()
        return task

    def delete_task(self, task_id: UUID) -> bool:
        task = self.storage.get(task_id)
        if not task:
            return False
        self.storage.delete(task_id)
        return True

    def toggle_task(self, task_id: UUID) -> Task | None:
        task = self.storage.get(task_id)
        if not task:
            return None
        task.toggle()
        return task

    def complete_task(self, task_id: UUID) -> Task | None:
        task = self.storage.get(task_id)
        if not task:
            return None
        task.completed = True
        task.updated_at = datetime.utcnow()
        return task

    def incomplete_task(self, task_id: UUID) -> Task | None:
        task = self.storage.get(task_id)
        if not task:
            return None
        task.completed = False
        task.updated_at = datetime.utcnow()
        return task
