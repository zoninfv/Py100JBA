import json


FILENAME = "input.json"


def task() -> list[dict]:
    with open(FILENAME, encoding="utf-8") as f:
        json_data = json.load(f)



        return sorted(json_data, key=lambda p: p["id"])


if __name__ == '__main__':
    # Необходимо для проверки
    data = task()
    print(json.dumps(data, indent=4))
