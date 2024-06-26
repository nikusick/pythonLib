"""
GeometryLib
----
Библиотека для работы с геометрическими фигурами
----
Пояснения к работе:
1) В работе опиралась на библиотеку scipy.stats, тк совсем недавно с ней работала в рамках учебы.
Именно поэтому классы написаны не в CamelCase: но я знаю, что по всем правилам классы оформляются именно так.

2) В работе были написаны три декоратора для проверки входных данных.

3) Площадь треугольника мы можем посчитать по 3-м сторонам, но сделать это с любой n-угольной фигурой мы не можем,
тк фигура перестает быть жесткой. Поэтому был написан класс n_gon_figures,
где площадь считается с помощью координат вершин фигуры.
В методе используется формула Гаусса, которая работает на выпуклых и вогнутых фигурах.
Единственное, надо вводить координаты вершин против часовой стрелки.

4) Отдельно был написан класс regular_n_gon_figures: класс правильных многоугольников.
Здесь площадь высчитывается с помощью количества вершин фигуры и длины его стороны.

5) Таким образом, наследуясь от n_gon_figures или regular_n_gon_figures, можно добавлять любые фигуры и считать
их площадь. Исключение составят круги, для которых был написан отдельный класс circle.
"""
from .figures import circle, n_gon_figures, regular_n_gon_figures, triangle
