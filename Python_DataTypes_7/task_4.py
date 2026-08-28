# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}
# Ваш код здесь

# Convert list to a set to remove duplicates
requested_roles_set = set(requested_roles)

# Find intersecting and missing roles
inter_roles = requested_roles_set.intersection(required_admin_roles)
diff_roles = required_admin_roles.difference(requested_roles_set)

# Check security_officer role in request
role_sec_off = "security_officer" in requested_roles_set

print(f"Уникальные запрошенные роли: {requested_roles_set}")
print(f"Общие административные роли: {inter_roles}")
print(f"Недостающие административные роли: {diff_roles}")
print(f"Наличие роли security_officer в запросе: {role_sec_off}")
