class TaskManager:
    def __init__(self, user_name):
        self.user_name = user_name
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)
        print(f"Added: {task_name}")

    def show_tasks(self):
        print(f"\n--- {self.user_name}'s Task List ---")
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

# Example usage
my_manager = TaskManager("Sonu")
my_manager.add_task("Review Git commands")
my_manager.add_task("Practice Python OOP")
my_manager.show_tasks()