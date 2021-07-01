from utils import read_csv, save_data_to_json

data = read_csv("data.csv")

json_output = []
for row in data:
    intent = row[0]
    entities = str(row[1]).split("\n")

    formatted_entities = []
    for entity in entities:
        label, value = entity.rsplit(".", 1)
        formatted_entities.append({"entity": label, "value": value})

    output = {}
    output["intent"] = intent
    output["entities"] = formatted_entities

    json_output.append(output)

save_data_to_json(json_output, "output")