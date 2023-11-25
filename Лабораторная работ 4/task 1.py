import json


FAIL = "input.json"


def task() -> float:
    with open(FAIL) as f:
        k = json.load(f)
        value = [item["score"] * item["weight"] for item in k]

    return round(sum(value), 3)


print(task())
