from flask import Flask, Response
from db_logic import get_config

app = Flask(__name__)

@app.route("/config", methods=["GET"])
def fetch_config():
    data = get_config()
    formatted_output = format_config_as_yaml(data)
    return Response(formatted_output, mimetype='text/plain')

def format_config_as_yaml(config):
    output = "Configuration File Parser Results:\n\n"
    for section, values in config.items():
        output += f"{section}:\n"
        for key, value in values.items():
            output += f"- {key}: {value}\n"
        output += "\n"
    return output.strip()