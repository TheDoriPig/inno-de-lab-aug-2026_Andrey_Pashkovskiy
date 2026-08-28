# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]
# Реализация конвейера агрегации метрик
# Ваш код здесь

active_nodes = []
cpu_loads = []
ram_usages = []

# Unpack tuple elements and filter online servers
for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "online":
        active_nodes.append(node_name)
        cpu_loads.append(cpu_load)
        ram_usages.append(ram_usage)

# Calculate metrics
nodes_count = len(active_nodes)
avg_cpu = round(sum(cpu_loads) / len(active_nodes), 2)
high_ram = max(ram_usages)

tele_report = {
    "active_nodes_count": nodes_count, 
    "metrics" : {
        "average_cpu": avg_cpu, 
        "max_ram": high_ram
    }
}

print(f"Активные узлы в сети: {active_nodes}")
print(f"Итоговый отчет телеметрии: {tele_report}")
