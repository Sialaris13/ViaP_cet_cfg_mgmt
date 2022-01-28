from jinja2 import Environment, FileSystemLoader
import yaml
import os


def load_data():
    data = {}
    for file in os.listdir("data"):
        with open(f"data/{file}") as f:
            d = yaml.safe_load(f)
            data.update(d)
    return data


def render(template: str, data: dict):
    template_env = Environment(loader=FileSystemLoader("templates"))
    template = template_env.get_template(template)
    output = template.render(**data)

    # remove all empty lines from file
    output = "\n".join([l for l in output.splitlines() if l.strip()])
    return output


def write_config(config, file):
    with open(f"config/{file}", "w") as f:
        f.write(config)
