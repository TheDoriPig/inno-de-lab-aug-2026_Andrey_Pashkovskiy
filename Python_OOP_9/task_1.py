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


# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 4. Проверка валидации (попытка задать неверный тип или 
# отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")
