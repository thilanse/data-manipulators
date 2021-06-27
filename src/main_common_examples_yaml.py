from utils import read_csv, save_data_to_yaml, convert_to_yaml_literal


data = read_csv("data.csv")

common_examples = {}
common_examples["version"] = "2.0"
common_examples["nlu"] = []

intent_examples_map = {}
for row in data:
    query = str(row[0])
    intent = str(row[1])
    
    if len(row) > 2:
        entities = row[1:]

    if intent not in intent_examples_map:
        intent_examples_map[intent] = []
    
    intent_examples_map[intent].append(query)

for intent, examples in intent_examples_map.items():
    common_example = {}
    common_example["intent"] = intent
    common_example["examples"] = convert_to_yaml_literal(examples)
    common_examples["nlu"].append(common_example)


save_data_to_yaml(common_examples, "nlu.yml")