import json
from database import DataBase


class JsonParser:
    def __init__(self):
        self.screen = ""
        self.palette = ""
        self.figures = ""
        self.database = DataBase()

    def parse_json(self, path):
        try:

            with open(path) as information:
                data = json.load(information)

            for label in self.database.types:
                if label not in data:
                    print("Json file doesn't have enough information! Screen, Palette and Figures are required!")
                    exit(1)

            self.screen = data['Screen']
            self.palette = data['Palette']
            self.figures = data['Figures']
            return self.screen, self.palette, self.figures

        except json.decoder.JSONDecodeError:
            print("Error while parsing json file!")
            exit(1)
        except FileNotFoundError:
            print("wrong path to the json file!")
            exit(1)
