import inquirer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.theme import Theme
from rich.live import Live
from src.manager import TodoManager

# Custom theme for a premium feel
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "dim": "grey50",
    "header": "bold magenta"
})

console = Console(theme=custom_theme)
manager = TodoManager()

def display_tasks(tasks_to_display=None):
    tasks = tasks_to_display if tasks_to_display is not None else manager.get_all_tasks()
    
    if not tasks:
        console.print(Panel("[warning]No tasks found. Start by adding one![/warning]", border_style="dim"))
        return

    table = Table(title="Your Todo Dashboard", header_style="header", border_style="dim", expand=True)
    table.add_column("ID", style="info", no_wrap=False, width=38)
    table.add_column("Status", justify="center", width=8)
    table.add_column("Title", style="bold white")
    table.add_column("Description", style="dim")
    table.add_column("Created At", style="dim", width=16)

    for task in tasks:
        status = "[success]✔[/success]" if task.completed else "[error]✘[/error]"
        description = task.description if task.description else "[dim]No description[/dim]"
        table.add_row(
            str(task.id),
            status,
            task.title,
            description,
            task.created_at.strftime("%Y-%m-%d %H:%M")
        )
    
    console.print(table)

def add_task_flow():
    questions = [
        inquirer.Text('title', message="Task Title", validate=lambda _, x: len(x.strip()) > 0),
        inquirer.Text('description', message="Task Description (optional)")
    ]
    answers = inquirer.prompt(questions)
    if answers:
        task = manager.add_task(answers['title'], answers['description'])
        console.print(f"[success]Task added successfully! ID: {task.id}[/success]")

def update_task_flow():
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print("[warning]No tasks to update.[/warning]")
        return

    choices = [(f"{t.title} ({str(t.id)[:8]})", t.id) for t in tasks]
    questions = [
        inquirer.List('task_id', message="Select task to update", choices=choices),
        inquirer.Text('title', message="New Title (leave blank to keep current)"),
        inquirer.Text('description', message="New Description (leave blank to keep current)"),
        inquirer.Confirm('toggle', message="Toggle completion status?", default=False)
    ]
    answers = inquirer.prompt(questions)
    if answers:
        task = manager.get_task_by_id(str(answers['task_id']))
        new_title = answers['title'] if answers['title'].strip() else None
        new_description = answers['description'] if answers['description'].strip() else None
        new_status = (not task.completed) if answers['toggle'] else None
        
        updated = manager.update_task(str(answers['task_id']), new_title, new_description, new_status)
        if updated:
            console.print(f"[success]Task updated successfully![/success]")

def delete_task_flow():
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print("[warning]No tasks to delete.[/warning]")
        return

    choices = [(f"{t.title} ({str(t.id)[:8]})", t.id) for t in tasks]
    questions = [
        inquirer.List('task_id', message="Select task to delete", choices=choices),
        inquirer.Confirm('confirm', message="Are you sure?", default=False)
    ]
    answers = inquirer.prompt(questions)
    if answers and answers['confirm']:
        if manager.delete_task(str(answers['task_id'])):
            console.print(f"[success]Task deleted successfully![/success]")

def toggle_task_flow():
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print("[warning]No tasks to toggle.[/warning]")
        return

    choices = [(f"[{'✔' if t.completed else ' '}] {t.title}", t.id) for t in tasks]
    questions = [
        inquirer.List('task_id', message="Select task to toggle completion", choices=choices)
    ]
    answers = inquirer.prompt(questions)
    if answers:
        if manager.toggle_task_status(str(answers['task_id'])):
            console.print(f"[success]Task status toggled![/success]")

def main():
    console.print(Panel.fit(
        "[bold magenta]The Evolution of Todo[/bold magenta]\n[dim]Phase I: In-Memory Management[/dim]",
        border_style="magenta"
    ))

    while True:
        questions = [
            inquirer.List('action',
                message="What would you like to do?",
                choices=[
                    ('View Tasks', 'view'),
                    ('Add Task', 'add'),
                    ('Update Task', 'update'),
                    ('Toggle Completion', 'toggle'),
                    ('Delete Task', 'delete'),
                    ('Exit', 'exit')
                ]
            )
        ]
        
        answers = inquirer.prompt(questions)
        if not answers or answers['action'] == 'exit':
            console.print("[info]Goodbye![/info]")
            break
        
        action = answers['action']
        if action == 'view':
            display_tasks()
        elif action == 'add':
            add_task_flow()
        elif action == 'update':
            update_task_flow()
        elif action == 'toggle':
            toggle_task_flow()
        elif action == 'delete':
            delete_task_flow()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[info]Interrupted. Exiting...[/info]")