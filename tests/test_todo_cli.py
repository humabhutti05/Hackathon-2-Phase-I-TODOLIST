import pytest
from src.manager import TodoManager
from src.todo.models import Task
from datetime import datetime
import uuid

def test_add_task():
    manager = TodoManager()
    task = manager.add_task("Buy groceries", "Milk, Eggs, Bread")
    assert task.title == "Buy groceries"
    assert task.description == "Milk, Eggs, Bread"
    assert not task.completed
    assert isinstance(task.id, uuid.UUID)
    assert len(manager.get_all_tasks()) == 1

def test_get_all_tasks():
    manager = TodoManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == task1.id  # Should be ordered by creation
    assert tasks[1].id == task2.id

def test_get_task_by_id():
    manager = TodoManager()
    task = manager.add_task("Find me")
    found_task = manager.get_task_by_id(task.id)
    assert found_task is not None
    assert found_task.id == task.id
    assert manager.get_task_by_id(str(uuid.uuid4())) is None

def test_update_task():
    manager = TodoManager()
    task = manager.add_task("Old Title", "Old Description")
    
    updated_task = manager.update_task(task.id, "New Title", "New Description", True)
    assert updated_task is not None
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"
    assert updated_task.completed
    assert updated_task.updated_at > task.created_at

def test_update_task_partial():
    manager = TodoManager()
    task = manager.add_task("Title", "Description")
    updated_task = manager.update_task(task.id, title="Only Title Updated")
    assert updated_task.title == "Only Title Updated"
    assert updated_task.description == "Description"
    assert not updated_task.completed

def test_update_non_existent_task():
    manager = TodoManager()
    assert manager.update_task(str(uuid.uuid4()), "Title") is None

def test_delete_task():
    manager = TodoManager()
    task = manager.add_task("Delete me")
    assert manager.delete_task(task.id)
    assert len(manager.get_all_tasks()) == 0
    assert manager.get_task_by_id(task.id) is None

def test_delete_non_existent_task():
    manager = TodoManager()
    manager.add_task("Keep me")
    assert not manager.delete_task(str(uuid.uuid4()))
    assert len(manager.get_all_tasks()) == 1

def test_complete_task():
    manager = TodoManager()
    task = manager.add_task("Incomplete task")
    assert not task.completed
    
    completed_task = manager.complete_task(task.id)
    assert completed_task is not None
    assert completed_task.completed

def test_incomplete_task():
    manager = TodoManager()
    task = manager.add_task("Complete task")
    manager.complete_task(task.id) # Mark as complete first
    assert task.completed
    
    incomplete_task = manager.incomplete_task(task.id)
    assert incomplete_task is not None
    assert not incomplete_task.completed

def test_complete_non_existent_task():
    manager = TodoManager()
    assert manager.complete_task(str(uuid.uuid4())) is None

def test_incomplete_non_existent_task():
    manager = TodoManager()
    assert manager.incomplete_task(str(uuid.uuid4())) is None
