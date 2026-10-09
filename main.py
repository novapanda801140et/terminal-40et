"""Terminal task manager."""
import json, os, sys

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as f: return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f: json.dump(tasks, f, indent=2)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
    for i, t in enumerate(tasks, 1):
        status = '✔' if t.get('completed') else '✖'
        print(f"{i}. [{status}] {t['text']}")

def add_task(text):
    tasks = load_tasks()
    tasks.append({'text': text, 'completed': False})
    save_tasks(tasks); print("Added.")

def complete_task(idx):
    tasks = load_tasks()
    if 1 <= idx <= len(tasks):
        tasks[idx-1]['completed'] = True
        save_tasks(tasks); print("Completed.")
    else:
        print("Invalid index.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: list|add|complete")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'list':
        list_tasks()
    elif cmd == 'add':
        if len(sys.argv) < 3:
            print("Task text required.")
            sys.exit(1)
        add_task(' '.join(sys.argv[2:]))
    elif cmd == 'complete':
        if len(sys.argv) < 3:
            print("Index required.")
            sys.exit(1)
        try:
            complete_task(int(sys.argv[2]))
        except ValueError:
            print("Index must be integer.")
    else:
        print("Unknown command.")