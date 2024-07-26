def read_conclusion_id():
    try:
        with open('data/conclusion_id.txt', 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 1


def write_conclusion_id(conclusion_id):
    with open('data/conclusion_id.txt', 'w') as file:
        file.write(str(conclusion_id))


def save_conclusions(source_page, text):
    conclusion_id = read_conclusion_id()

    with open('data_insight/conclusions.txt', 'a') as file:
        if source_page:
            file.write(f'{conclusion_id}-{source_page} {text}\n')
        else:
            file.write(f'{conclusion_id}-{text}\n')

    conclusion_id += 1
    write_conclusion_id(conclusion_id)


def clear_file(filepath):
    with open(filepath, 'w') as _:
        pass


def get_conclusions():
    conclusions = []

    try:
        with open('data_insight/conclusions.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split('-', 1)
                if len(parts) > 1:
                    text = parts[1].strip()
                    conclusions.append([parts[0], text])
    except FileNotFoundError:
        message = "No conclusions file found."
        print(message)
    return conclusions
