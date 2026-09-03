from task_1 import Trainee


class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        """Always return True for audit trainees"""
        return True


class Cohort:
    def __init__(self, title: str, trainees: list[Trainee] | None = None):
        """Initialisation of a student group
            
        Args:
            title (str): Title of the group
            trainees (list[Trainee]): List of group members. Default to []
        """
        self.title = title
        self.trainees = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        """Add a new trainee into the group"""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """All group attend a lecture. Every trainee increase score"""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Makes list with trainee who pass the course"""
        return [trainee for trainee in self.trainees if trainee.is_passing()]


# 1. Создаем учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
print()
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}\n")

print("\nУспешно зачислены на следующий модуль:")
print()
for student in passing_students:
    print(f"- {student.name} {student.surname}\n")
    