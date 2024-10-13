result = None
team1_num = 1
team2_num = 100
team1_time = 1800
team2_time = 1800
score_1 = 52
score_2 = 88
tasks_total = score_1 + score_2
time_avg = tasks_total / (team1_time + team2_time)
challenge_result = "Волшебники данных"

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

print("В команде Мастера кода участников: %s ! " % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num,team2_num))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team2_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print( f"Результат битвы: {result}!")
