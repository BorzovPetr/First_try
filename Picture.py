import graph


def main():
    graph.windowSize(800, 600)
    beach(0, 450)
    sea(0, 330)
    sky(0, 0)
    cloud(100, 100, 20)
    sun(400, 100, 40)
    ship(250, 360, 150, 35)
    


def beach(x, y):
    """
        Рисует песчаный пляж.
        (x, y) -- координаты левой верхней точки прямоугольника-пляжа.
    """
    graph.brushColor('yellow')
    graph.penSize(0)
    graph.rectangle(x, y, x + 800, y + 150)


def sea(x, y):
    """
        Рисует море.
        (x, y) -- координаты левой верхней точки прямоугольника-моря.
    """
    graph.brushColor(30, 144, 255)
    graph.penSize(0)
    graph.rectangle(x, y, x + 800, y + 120)


def sky(x, y):
    """
        Рисует небо.
        (x, y) -- координаты левой верхней точки прямоугольника-неба.
    """
    graph.brushColor(173, 216, 230)
    graph.penSize(0)
    graph.rectangle(0, 0, x + 800, y + 330)


def cloud(x, y, r):
    """
        Рисует облако с круглыми перьями.
        (x, y) -- координаты центра окружности левого верхнего пера облака;
        r -- радиус пера облака. 
    """
    graph.brushColor('white')
    graph.penSize(2)
    number_of_feather = 4
    number_of_row = 2
    for i in range(number_of_feather):
        for j in range(number_of_row):
            graph.circle(x - 25*j + 25*i, y + 25*j, r)
    graph.circle(x - 25*number_of_row + 25*(number_of_feather + 1), y + 25*(number_of_row - 1), r)


def sun(x, y, r):
    """
        Рисует Солнце.
        (x, y) -- координаты центра окружности Солнца;
        r -- радиус Солнца.
    """
    graph.brushColor("yellow")
    graph.penSize(0)
    graph.circle(x, y, r)


def ship(x, y, deck_lenght, carcass_height):
    """
        Рисует корабль.
        (x, y) -- координаты правой верхней точки прямоугольника-палубы.
        deck_lenght, carcass_height -- длина прямоугольника-палубы и высота корпуса.
    """
    carcass(x, y, deck_lenght, carcass_height)
    mast(x, y, deck_lenght, carcass_height)
    sail(x, y, deck_lenght, carcass_height)


def carcass(x, y, deck_lenght, carcass_height):
    """
        Рисует корпус корабля.
        (x, y) -- координаты правой верхней точки прямоугольника-палубы.
        deck_lenght, carcass_height -- длина прямоугольника-палубы и высота корпуса.
    """
    graph.brushColor(139, 69, 19)
    graph.penSize(0)
    graph.rectangle(x, y, x + deck_lenght, y + carcass_height)
    graph.brushColor(139, 69, 19)
    graph.penSize(0)
    graph.polygon([(x + deck_lenght, y), (x + deck_lenght, y + carcass_height), (x + 1.5*deck_lenght, y), (x + deck_lenght, y)])
    graph.brushColor(139, 69, 19)
    graph.penSize(0)
    graph.arc(x + carcass_height, y - carcass_height, x - carcass_height, y + carcass_height, -180, -90)
    graph.brushColor('black')
    graph.circle(x + 1.1*deck_lenght, y + 0.4*carcass_height, carcass_height/4.5)
    graph.brushColor('white')
    graph.circle(x + 1.1 * deck_lenght, y + 0.4 * carcass_height, carcass_height / 6.5)



def mast(x, y, deck_lenght, carcass_height):
    """
        Рисует мачту.
        (x, y) -- координаты правой верхней точки прямоугольника-палубы.
        deck_lenght, carcass_height -- длина прямоугольника-палубы и высота корпуса.
    """
    graph.brushColor('black')
    graph.rectangle(x + deck_lenght/3, y, x + 0.03*deck_lenght +deck_lenght/3, y - 2.5*carcass_height)


def sail(x, y, deck_lenght, carcass_height):
    """
           Рисует двойной парус.
           (x, y) -- координаты правой верхней точки прямоугольника-палубы.
           deck_lenght, carcass_height -- длина прямоугольника-палубы и высота корпуса.
       """
    graph.brushColor('white')
    graph.polygon([(x + 0.03*deck_lenght + deck_lenght/3, y), (x + 0.8*deck_lenght, y - 2.5*carcass_height/2),
                   (x + 0.12*deck_lenght + deck_lenght/3, y - 2.5*carcass_height/2), (x + 0.03*deck_lenght + deck_lenght/3, y)])
    graph.polygon([(x + 0.03*deck_lenght + deck_lenght / 3, y - 2.5*carcass_height), (x + 0.8 * deck_lenght, y - 2.5 * carcass_height / 2),
                   (x + 0.12*deck_lenght + deck_lenght / 3, y - 2.5 * carcass_height / 2), (x + 5 + deck_lenght / 3, y - 2.5*carcass_height)])




main()

graph.run()
