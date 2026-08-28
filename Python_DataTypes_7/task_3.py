# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Ваш код здесь

# Extract host and port from connection
db_host = db_config.get("connection").get("host")
db_port = db_config.get("connection").get("port")

# Check for ssl_settings and ssl_mode with a default value
db_ssl_settings = db_config.get("ssl_settings", {}).get("ssl_mode", "verify-full")

# Update user to admin
db_config["connection"]["user"] = "admin"
# Add max_connections parameter
db_config["connection"]["max_connections"] = 100

print(f"SSL Mode: {db_ssl_settings}")
print("Параметры соединения:")

for k, v in db_config["connection"].items():
    print(f"* {k}: {v}")
