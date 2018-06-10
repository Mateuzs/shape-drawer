from PIL import Image as NewImage
from libs.graphics import *


class ShapeDrawer:

    def __init__(self, screen, palette, figure, image_name):
        try:
            self.screen = screen
            self.palette = palette
            self.image_name = image_name
            self.win = GraphWin('Shape', screen.get('width'), screen.get('height'))
            self.figure = figure
            self.shape = None
            self.color = self._set_color()
            if self.figure.get('type') != 'polygon':
                try:
                    self.centerPoint = Point(self.figure.get('x'), self.figure.get('y'))
                except TypeError:
                    print(self.figure.get('type'),
                          " : There is missing some information about the center point in figure!")

        except TypeError:
            print(self.figure.get('type'), " : There is missing some information about the screen!")
            exit(1)

    def draw(self, shape):
        try:
            background = Rectangle(Point(0, 0), Point(self.screen.get("width"), self.screen.get("height")))

            if "bg_color" in self.screen:
                background.setFill(self.palette.get(self.screen.get("bg_color")))
            else:
                background.setFill('black')

            self.shape = shape
            self.shape.setFill(self.color)
            background.draw(self.win)
            self.shape.draw(self.win)

            if self.image_name != "empty":
                self.win.postscript(file=self.image_name, colormode='color')
                img = NewImage.open(self.image_name)
                img.save(self.image_name)

            self.win.getMouse()
            self.win.close()

        except GraphicsError:
            print("Closed the window on demand")
            exit(0)

    def _set_color(self):
        try:
            if 'color' in self.figure:
                return self._read_color(self.palette.get(self.figure.get('color')))
            elif 'fg_color' in self.screen:
                return self._read_color(self.palette.get(self.screen.get('fg_color')))
            else:
                return 'white'

        except TypeError:
            print(self.figure.get('type'), ": There is missing some information about colors in palette!")

    def _read_color(self, color):
        chars = [chr(i) for i in range(97, 123)]
        if color[0] == '#' or color[0] in chars:
            return color
        elif color[0] == '(':
            my_tuple = self._translate_tuple(color)
            return color_rgb(my_tuple[0], my_tuple[1], my_tuple[2])
        else:
            print(self.figure.get('type'), " : Parsing color error, wrong type of color!")

    @staticmethod
    def _translate_tuple(char_tuple):

        variables = [chr(i) for i in range(48, 57)]
        number_array = []
        number = ""

        for character in char_tuple:
            if character in variables:
                number += character
            elif character in [',', ')']:
                number_array.append(int(number))
                number = ""

        return number_array


class CircleDrawer(ShapeDrawer):

    def __init__(self, screen, palette, figure, image_name):
        ShapeDrawer.__init__(self, screen, palette, figure, image_name)

    def draw_circle(self):
        if self.figure.get('type') != 'circle':
            print(self.figure.get('type'), ' : wrong type of figure!')
            return
        try:
            shape = Circle(self.centerPoint,
                           self.figure.get('radius')
                           )

            self.draw(shape)

        except TypeError:
            print(self.figure.get('type'), " : There is missing some information about figure!")
        except AttributeError:
            print(self.figure.get('type'), " : There is missing some information about figure!")


class PointDrawer(ShapeDrawer):

    def __init__(self, screen, palette, figure, image_name):
        ShapeDrawer.__init__(self, screen, palette, figure, image_name)

    def draw_point(self):
        if self.figure.get('type') != 'point':
            print(self.figure.get('type'), ' : wrong type of figure!')
            return
        try:
            shape = self.centerPoint
            self.draw(shape)

        except TypeError:
            print(self.figure.get('type'), " : There is missing some information about figure!")


class RectangleDrawer(ShapeDrawer):

    def __init__(self, screen, palette, figure, image_name):
        ShapeDrawer.__init__(self, screen, palette, figure, image_name)

    def draw_rectangle(self):
        if self.figure.get('type') != 'rectangle' and self.figure.get('type') != 'square':
            print(self.figure.get('type'), ' : wrong type of figure!')
            return
        try:
            if self.figure.get('type') == 'rectangle':

                shape = Rectangle(Point(self.centerPoint.getX() - self.figure.get('width')/2,
                                        self.centerPoint.getY() - self.figure.get('height')/2),
                                  Point(self.centerPoint.getX() + self.figure.get('width')/2,
                                        self.centerPoint.getY() + self.figure.get('height')/2)
                                  )
            else:
                shape = Rectangle(Point(self.centerPoint.getX() - self.figure.get('length')/2,
                                        self.centerPoint.getY() - self.figure.get('length')/2),
                                  Point(self.centerPoint.getX() + self.figure.get('length')/2,
                                        self.centerPoint.getY() + self.figure.get('length')/2)
                                  )
            self.draw(shape)

        except TypeError:
            print(self.figure.get('type'), " : There is missing some information about figure!")


class PolygonDrawer(ShapeDrawer):

    def __init__(self, screen, palette, figure, image_name):
        ShapeDrawer.__init__(self, screen, palette, figure, image_name)

    def draw_polygon(self):
        if self.figure.get('type') != 'polygon':
            print(self.figure.get('type'), ' : wrong type of figure!')
            return
        try:
            points = []

            for point in self.figure.get("points"):
                points.append(Point(point[0], point[1]))

            polygon = Polygon(points)
            self.draw(polygon)

        except TypeError:
            print(self.figure.get('type'), " : There is missing some information about figure!")
