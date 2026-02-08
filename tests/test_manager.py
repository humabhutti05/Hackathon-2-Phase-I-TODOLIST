import pytest
from src.manager import TodoManager

def test_add_task():
    manager = TodoManager()
    task = manager.add_task("Test Title", "Test Description")
    assert len(manager.get_all_tasks()) == 1
    assert task.title == "Test Title"
    assert task.completed is False

def test_update_task():
    manager = TodoManager()
    task = manager.add_task("Old Title", "Old Desc")
    manager.update_task(task.id, title="New Title")
    assert task.title == "New Title"
    assert task.description == "Old Desc"

def test_delete_task():
    manager = TodoManager()
    task = manager.add_task("To Delete", "")
    assert len(manager.get_all_tasks()) == 1
    manager.delete_task(task.id)
    assert len(manager.get_all_tasks()) == 0

def test_toggle_status():
    manager = TodoManager()
    task = manager.add_task("Toggle Me", "")
    assert task.completed is False
    manager.toggle_task_status(task.id)
    assert task.completed is True
    manager.toggle_task_status(task.id)
    assert task.completed is False
