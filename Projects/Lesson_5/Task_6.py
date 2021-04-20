
if __name__ == "__main__":
    subjects = {}

    try:
        with open('to_task_6.txt') as fh:
            lines = fh.readlines()

        for line in lines:
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные данные")

    print(subjects)
