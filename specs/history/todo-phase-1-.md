# Specification: Phase I - Todo In-Memory Python Console App

## Objective
Build a command-line todo application that stores tasks in memory.

## Features
1. **Add Task**:
   - Required fields: Title, Description.
   - Auto-generated: ID (unique), Status (default: Incomplete), Created At.
2. **View Tasks**:
   - List all tasks in a table format.
   - Show status indicators (e.g., icons or colors).
3. **Update Task**:
   - Edit Title and Description of an existing task by ID.
4. **Delete Task**:
   - Remove a task from memory by ID.
5. **Mark Complete**:
   - Toggle status between Complete and Incomplete.

## Technical Requirements
- UI: `rich` and `inquirer`.
- State: In-memory list of dictionaries/objects.
- Python: 3.13+.
- Entry point: `app` (via `pyproject.toml`).

## Success Criteria
- All 5 features work as expected.
- Input is validated (e.g., non-empty titles).
- Table output is clear and aesthetically pleasing.
