import os
import json

def log(article, core_message, abstract_depiction):
    if not os.path.exists("log.json"):
        with open("log.json", "w") as log_file:
            json.dump([], log_file)

    with open("log.json") as log_file:
        log_data = json.load(log_file)
    log_data.append({
        "article": article,
        "core_message": core_message,
        "abstract_depiction": abstract_depiction
    })
    with open("log.json", "w") as log_file:
        json.dump(log_data, log_file)