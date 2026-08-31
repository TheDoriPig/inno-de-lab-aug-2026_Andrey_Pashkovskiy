from typing import Callable, Any
import time

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


# Created decorator
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """A decorator displays function execution time

    Args:
        func: The function to be monitored

    Returns:
        The wrapped function
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        time_work = time.perf_counter() - start_time

        print(
            f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}'"
            f" выполнена за {time_work:.{TIME_DECIMALS}f} сек."
        )

        return result
    return wrapper


# Apply the decorator
@performance_logger
def get_sorted_report(
    arg: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Sorts category total sales in descending order

    Args:
        arg: A list containing category and total sales

    Returns:
        The sorted list of categories
    """
    result = sorted(arg, key=lambda x: float(x["total_sales"]), reverse=True)
    return result


# Dataset from task
dataset_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]

dataset_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]

dataset_3 = [{"category": "Drama", "total_sales": 500.00}]


# Output the result
print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===\n")

print("\n--- Тест 1 ---")
sorted_report = get_sorted_report(dataset_1)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_report, start=1):
    print(f"{i}. {item["category"]}: {item["total_sales"]}")

print("\n--- Тест 2 ---")
sorted_report = get_sorted_report(dataset_2)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_report, start=1):
    print(f"{i}. {item["category"]}: {item["total_sales"]}")

print("\n--- Тест 3 ---")
sorted_report = get_sorted_report(dataset_3)
print("Топ категорий по выручке:")
for i, item in enumerate(sorted_report, start=1):
    print(f"{i}. {item["category"]}: {item["total_sales"]}")
