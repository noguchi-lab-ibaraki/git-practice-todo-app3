import json
import sys

# シンプルなToDoリストを管理するクラス
class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        # 未実装：タスクをリストに追加する機能
        self.save_tasks()
        pass

    def list_tasks(self):
        # 未実装：リスト内のタスクを表示する機能
        for i in self.tasks:
            print(self.tasks.index(i) + ': ' + i)

    def remove_task(self, task_number):
        # 未実装：指定されたタスクをリストから削除する機能
        self.save_tasks()
        pass

    def complete_task(self, task_number):
        # 未実装：指定されたタスクを完了済みとしてマークする機能
        pass

def print_help():
    print("Usage:")
    print("  python todo.py add <task>")
    print("  python todo.py list")
    print("  python todo.py remove <task_number>")
    print("  python todo.py complete <task_number>")
    print("  python todo.py help")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]
    todo_list = ToDoList()

    match command:
        case "add":
            if len(sys.argv) != 3:
                print("Error: Task description is required.")
            else:
                task = sys.argv[2]
                todo_list.add_task(task)
        case "list":
            todo_list.list_tasks()
        case "remove":
            if len(sys.argv) != 3:
                print("Error: Task number is required.")
            else:
                try:
                    task_number = int(sys.argv[2])
                    todo_list.remove_task(task_number)
                except ValueError:
                    print("Error: Task number must be an integer.")
        case "complete":
            if len(sys.argv) != 3:
                print("Error: Task number is required.")
            else:
                try:
                    task_number = int(sys.argv[2])
                    todo_list.complete_task(task_number)
                except ValueError:
                    print("Error: Task number must be an integer.")
        case _:
            print_help()

if __name__ == "__main__":
    main()
