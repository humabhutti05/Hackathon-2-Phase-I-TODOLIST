# Claude Code Instructions

## Project Context
Building "The Evolution of Todo". Phase I is an in-memory Python console app.

## Commands
- Run app: `uv run app`
- Run tests: `uv run pytest`
- Add dependencies: `uv add <pkg>`

## Coding Style
- Follow PEP 8 convention.
- Use type hints for all functions.
- Keep functions small and focused on a single responsibility.
- Use `rich` for all terminal UI elements.
- Use `inquirer` for all user input prompts.

## Workflow
1. Read the specification in `specs/`.
2. Update `specs/history` with a timestamped version before making changes.
3. Implement the changes in `src/`.
4. Run tests and verify functionality.
