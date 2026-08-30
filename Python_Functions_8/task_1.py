MAX_RENTAL_BATCH_LIMIT = 150.0


# Created function to calculate the rental batch
def calculate_rental_batch(quantity: int, rental_rate: float,
                            discount: float = 0.0) -> tuple[float, bool]:
    """Calculates the total rental batch cost with a discount

    Args:
        quantity: The number of discs in the batch
        rental_rate: The rental price per single disc
        discount: The percentage of genre discount
    
    Returns:
        A tuple containing the final sum and a limit excess flag
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return (final_sum, is_limit_exceeded)


# Output the result
print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

rental_batch = calculate_rental_batch(30, 2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма {rental_batch[0]}$."
      f" Превышение лимита: {rental_batch[1]}"
)

# Function call with named arguments
rental_batch = calculate_rental_batch(
    quantity=40, rental_rate=4.99, discount=0.10
)
print(f"Партия 2 (Affair Prejudice): Сумма {rental_batch[0]}$."
      f" Превышение лимита: {rental_batch[1]}"
)

rental_batch = calculate_rental_batch(10, 1.99)
print(f"Партия 3 (Agent Truman): Сумма {rental_batch[0]}$."
      f" Превышение лимита: {rental_batch[1]}"
)

rental_batch = calculate_rental_batch(50, 3.50, 0.20)
print(f"Партия 4 (African Egg): Сумма {rental_batch[0]}$."
      f" Превышение лимита: {rental_batch[1]}"
)
