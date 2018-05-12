from json_parser import JsonParser
from shape_drawer import CircleDrawer, SquareDrawer, RectangleDrawer, PointDrawer, PolygonDrawer
from database import DataBase
import argparse
import sys


def main(args):




    parser = argparse.ArgumentParser()
    parser.add_argument("-a", nargs=1, action="store", dest="json_file_name", default=["empty"])
    parser.add_argument("-o", nargs=1, action="store", dest="image_name", default=["empty"])
    parser.add_argument("--output", nargs=1, action="store", dest="image_name", default=["empty"])
    parsed_args = parser.parse_args(args)

    image_name = parsed_args.image_name[0]
    json_file_name = parsed_args.json_file_name[0]

    if json_file_name == "empty":
        print("\n Welcome to my shape drawer :)\n"
              " you can use following options:\n\n"
              "  -a <json-file-name> : path to json file describing the shape or shapes\n"
              "  -o | --output <image-name.png> : allows to save your drawing\n\n"
              " working examples:\n\n"
              " python main.py -a data.json\n"
              " python main.py -a image.json -o star.png\n")
        exit(0)

    json_parser = JsonParser()
    screen, palette, figures = json_parser.parse_json(json_file_name)
    database = DataBase()

    for figure in figures:
        figure_name = figure.get('type')
        if figure_name in database.figures:

            if figure_name == 'circle':

                    shape = CircleDrawer(screen, palette, figure, image_name)
                    shape.draw_circle()

            elif figure_name == 'square':

                    shape = SquareDrawer(screen, palette, figure, image_name)
                    shape.draw_square()

            elif figure_name == 'rectangle':

                    shape = RectangleDrawer(screen, palette, figure, image_name)
                    shape.draw_rectangle()

            elif figure_name == 'point':

                    shape = PointDrawer(screen, palette, figure, image_name)
                    shape.draw_point()

            elif figure_name == 'polygon':

                    shape = PolygonDrawer(screen, palette, figure, image_name)
                    shape.draw_polygon()

            else:
                print("Unrecognized figure")
                exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
