from utils import read_csv, save_data_to_json, save_data_to_yaml

data = read_csv("data.csv")

common_examples = []
for row in data:
    example = {}
    example["text"] = row[0]
    example["intent"] = row[1]
    example["entities"] = []

    common_examples.append(example)

training_data = {
    "rasa_nlu_data":{
        "common_examples": common_examples,
        "regex_features": [],
        "entity_synonyms": []
    }
}

save_data_to_json(training_data, "nlu.json")



