import yaml

with open("environment.yml", 'r') as stream:
    try:
        env_file = yaml.safe_load(stream)
        keys = env_file.get("keys")
        files = env_file.get("files")
    except yaml.YAMLError as exc:
        print(exc)


def apply_placeholders(line):
    for key in keys:
        line = line.replace(str("{{" + key + "}}"), str(keys[key]))
    return line


def parse_file(file_path):
    try:
        config_file = open(file_path, 'wt')
        example_file = open(file_path + ".example", 'r')

        for example_line in example_file:
            config_file.write(apply_placeholders(example_line))
    except FileNotFoundError:
        print("Il manque le fichier : " + file_path)


for file in files:
    parse_file(file)
