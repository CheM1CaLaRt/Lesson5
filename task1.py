class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print("Задача добавлена:", description)

    def mark_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.completed = True
                print("Задача отмечена как выполненная:", description)
                return
        print("Задача не найдена:", description)

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(f"Описание: {task.description}, Срок выполнения: {task.due_date}")
        else:
            print("Нет невыполненных задач.")

def main():
    manager = TaskManager()
    while True:
        print("\n1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать текущие задачи")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи (YYYY-MM-DD): ")
            manager.add_task(description, due_date)
        elif choice == '2':
            description = input("Введите описание выполненной задачи: ")
            manager.mark_as_completed(description)
        elif choice == '3':
            manager.show_current_tasks()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()