def robot_vacuum_agent(battery, dust_bin, motor_temperature):
    if motor_temperature > 45 and dust_bin > 90:
        return “Мотор қызып кетті және шаң жәшігі толды"
    elif motor_temperature > 45 and battery < 20:
        return "Мотор қызып кетті және батарея аз"
    elif battery < 20 and dust_bin > 90:
        return "Батарея аз және шаң жәшігі толды"
    elif motor_temperature > 45:
        return "Мотор қызып кетті"
    elif dust_bin > 90:
        return "Шаң жәшігін тазалау керек"
    elif battery < 20:
        return "Зарядтауға бару"
    else:
        return "Робот қалыпты жұмыс істеп тұр"
print(robot_vacuum_agent(80, 95, 50))
print(robot_vacuum_agent(10, 50, 50))
print(robot_vacuum_agent(10, 95, 30))
print(robot_vacuum_agent(80, 50, 50))
print(robot_vacuum_agent(80, 95, 30))
print(robot_vacuum_agent(10, 50, 30))
print(robot_vacuum_agent(80, 50, 30))
