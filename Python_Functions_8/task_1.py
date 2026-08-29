MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Args
    
    Returns
    """

    final_sum = round(quantity * rental_rate * (1 - discount), 2)

    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return (final_sum, is_limit_exceeded)

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
rental_batch = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {rental_batch[0]}. Превышение лимита: {rental_batch[1]}")
rental_batch = calculate_rental_batch(40, 4.99, 0.10)
print(f"Партия 2 (Affair Prejudice): Сумма {rental_batch[0]}. Превышение лимита: {rental_batch[1]}")
rental_batch = calculate_rental_batch(10, 1.99)
print(f"Партия 3 (Agent Truman): Сумма {rental_batch[0]}. Превышение лимита: {rental_batch[1]}")
rental_batch = calculate_rental_batch(50, 3.50, 0.20)
print(f"Партия 4 (African Egg): Сумма {rental_batch[0]}. Превышение лимита: {rental_batch[1]}")