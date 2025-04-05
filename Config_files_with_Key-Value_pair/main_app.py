from read_config import parse_config
from db_logic import save_config
from api_app import app

if __name__ == "__main__":
    try:
        config_path = "/Users/kanakamanojgarapati/MyPython_Projects/Config_files_with_Key-Value_pair/config/infra-details.ini"
        parsed_config = parse_config(config_path)
        save_config(parsed_config)
        print("Configuration parsed and saved to DB.")
        app.run(debug=True)
    except FileNotFoundError as fnf:
        print(f"{fnf}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
