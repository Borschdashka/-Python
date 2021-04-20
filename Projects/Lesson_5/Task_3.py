with open("to_task_3.txt", "r") as f:
    workers = {line.split()[0]: int(line.split()[1]) for line in f}
    print(f'Средняя зарплата сотрудников = {round(sum(workers.values()) / len(workers), 3)}\n'
      f'Сотрудники с зарплатой меньше 20000: {[i[0] for i in workers.items() if i[1] < 20000]}')
