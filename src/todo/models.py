from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Task:
    title: str
    description: str
    id: UUID = field(default_factory=uuid4)
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def toggle(self):
        self.completed = not self.completed
        self.updated_at = datetime.utcnow()
