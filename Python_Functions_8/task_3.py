from typing import Any


DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    movie_name: str, days_overdue: Any, fine_rate: float
) -> tuple[float, float] | None:
    """Calculates the overdue fine and return index from input data

    System stability is ensured by handling the following errors:
        - ValueError: Raised when string data cannot be cast to float.
        - ZeroDivisionError: Raised when overdue days equal zero.
        - TypeError: Raised when unsupported data types are passed.
    
    Args: 
        movie_name (str): The name of the movie
        days_overdue (Any): Raw input for overdue days
        fine_rate (float): The rate charged per single overdue day

    Returns:
        A tuple containing (total_fine, return_index) if successful, 
        or None if an error occurs
    """
    try:
        # Try to convert raw data into a float
        numeric_days = float(days_overdue) 

        # Calculate the total accumulated fine amount
        total_fine = numeric_days * fine_rate

        # Calculate the technical turnover index
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        # Print the successful transaction result
        print(f"Фильм: '{movie_name}' | Итоговый штраф: {total_fine}$ "
              f"| Индекс: {return_index}")
        return total_fine, return_index
    
    except TypeError:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_name}': "
              f"float() argument must be a string or a real number, "
              f"not '{type(days_overdue).__name__}'")
        return None
    
    except ValueError:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для "
              f"'{movie_name}': could not convert string to float: "
              f"'{days_overdue}'")
        return None
    
    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для "
              f"'{movie_name}': float division by zero")
        return None
    
    finally:
        print("\n--- Проверка транзакции возврата завершена ---\n\n") 
        # A lot \n to match the indentation in the example


print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")

calculate_overdue_fine("Matrix", 5, 1.5)

calculate_overdue_fine("Inception", "пять", 2.0)

calculate_overdue_fine("Avatar", 0, 2.5)

calculate_overdue_fine("Interstellar", [3,], 3.0)
