# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
# Ваш код здесь

# Split the string and strip whitespace from each element
split_user_record = raw_user_record.split(";")
strip_user_record = [s.strip() for s in split_user_record]

# Format fields according to requirements
strip_user_record[0] = f"UID-{strip_user_record[0]}"
strip_user_record[1] = strip_user_record[1].replace("_", " ").title()
strip_user_record[2] = strip_user_record[2].upper()
strip_user_record[3] = strip_user_record[3].lower()

# Join processed fields into a single formatted string
normalized_user_record = " | ".join(strip_user_record)

print(f"Нормализованная запись: {normalized_user_record}")
