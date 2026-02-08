from typing import Dict, List
from uuid import UUID
from src.todo.models import Task

class InMemoryTaskStorage:
    def __init__(self):
        self._tasks: Dict[UUID, Task] = {}

    def add(self, task: Task):
        self._tasks[task.id] = task

    def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    def get(self, task_id: UUID) -> Task | None:
        return self._tasks.get(task_id)

    def delete(self, task_id: UUID):
        self._tasks.pop(task_id, None)
