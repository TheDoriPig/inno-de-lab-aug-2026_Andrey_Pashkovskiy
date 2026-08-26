# Список транзакций, полученных от платежного шлюза

raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10","SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# Реализация фильтрации в одну строку с помощью List Comprehension
# Ваш код здесь

# Filter by SUCCESS status, extract amounts, and keep only positive integers
successful_sales = [int(t.split(":")[1]) for t in raw_transactions if t.startswith("SUCCESS") and int(t.split(":")[1]) > 0]

print(f"Очищенные транзакции: {successful_sales}")
