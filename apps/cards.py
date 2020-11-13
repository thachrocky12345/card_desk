class Card(object):
    def __init__(self, color, value):
        self.color = color
        self.value = value

    @property
    def color_point(self):
        return self.value * self.color.value

    def show(self):
        print("{} of {}".format(self.value, self.color.name))
