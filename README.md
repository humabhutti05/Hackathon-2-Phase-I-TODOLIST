# The Evolution of Todo - Phase I

## Overview
Phase I of "The Evolution of Todo" project. This is a command-line application built with Python 3.13+, focusing on in-memory task management.

## Features
- **Add**: Create tasks with titles and descriptions.
- **View**: List tasks in a beautiful table with status indicators.
- **Update**: Edit existing tasks.
- **Delete**: Remove tasks by their unique ID.
- **Mark Complete**: Toggle progress status.

## Tech Stack
- **Python 3.13+**
- **UV** (Package Manager)
- **Rich** (Terminal UI)
- **Inquirer** (Interactive Prompts)

## Installation & Setup
1. Ensure you are using WSL 2 (for Windows users).
2. Install `uv`:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. Sync dependencies:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run app
   ```

## Workflow
This project follows an Agentic Dev Stack workflow:
1. Write Spec
2. Generate Plan
3. Break into Tasks
4. Implement via Agent
