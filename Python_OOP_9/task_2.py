class Trainee:
    def __init__(
        self, name: str, surname: str, score: int = 0, passing_grade: int = 10
    ):
        """Initialisation a trainee in the educational platform
        Args:
            name (str): The first name of the trainee
            surname (str): The last name of the trainee
            score (int): Initial score. Default to 0
            passing_grade (int): Required score to pass the course. 
            Default to 10
        """
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self) -> int:
        """The current score"""
        return self.__score

    @score.setter
    def score(self, value: int):
        """Sets the trainee score
        
        Args: 
            value (int): The target score value to be set
        """
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        elif value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        else: 
            self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        """Compares the current score with the required score to pass the course"""
        return self.score >= self.passing_grade


class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        """Always return True for audit trainees"""
        return True


class Cohort:
    def __init__(self, title: str, trainees: list[Trainee] = []):
        """Initialisation a student group
            
        Args:
            title (str): Title of the froup
            trainees (list[Trainee]): List of group members. Default to []
        """
        self.title = title
        self.trainees = trainees

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