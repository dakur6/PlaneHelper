# SPDX-License-Identifier: MIT
# (c) 2026 dakur6

import command
import plane

VERSION = "0.1 Beta"
current_plane = None

class HelpCommand(command.Command):
    def __init__(self):
        super().__init__("help", "посмотреть список всех команд")

    def execute(self, args):
        print("Список доступных команд:")
        for name, instance in command.get_all().items():
            print(f" > {name}: {instance.get_description()}") 

class SetPlaneCommand(command.Command):
    def __init__(self):
        super().__init__("setplane", "задать новую плоскость", "setplane [x1] [y1] [z1] [x2] [y2] [z2] [x3] [y3] [z3]")

    def execute(self, args):
        global current_plane
        if(len(args) < 9):
            raise command.InvalideSyntaxCommandException()
        
        coords = list(map(float, args))
        p1 = (coords[0], coords[1], coords[2])
        p2 = (coords[3], coords[4], coords[5])
        p3 = (coords[6], coords[7], coords[8])

        try:
            current_plane = plane.Plane.from_points(p1, p2, p3)
            print(f"Плоскость {current_plane} успешно задана")
        except ValueError as e:
            print(f"Не удалось задать плоскость: {e}")

class PlaneCommand(command.Command):
    def __init__(self):
        super().__init__("plane", "показать информацию о текущей плоскости")

    def execute(self, args):
        if current_plane == None:
            print("Плоскость не задана. Используйте команду \"setplane\" чтобы задать плоскость")
            return
        
        print(f"Плоскость: {current_plane}")
        print(f"Вектор нормали плоскости: {current_plane.get_normal_vector()}")

class FindXCommand(command.Command):
    def __init__(self):
        super().__init__("x?", "найти координату X точки, лежащей в плоскости, по известным координатам Y и Z", "x? [Y] [Z]")

    def execute(self, args):
        if(len(args) < 2):
            raise command.InvalideSyntaxCommandException()
        
        if current_plane == None:
            print("Плоскость не задана. Используйте команду \"setplane\" чтобы задать плоскость")
            return
        
        y, z = list(map(float, args))
        try:
            print(f"X = {current_plane.find_x(y, z):.2f}")
        except ValueError as e:
            print(e)

class FindYCommand(command.Command):
    def __init__(self):
        super().__init__("y?", "найти координату Y точки, лежащей в плоскости, по известным координатам X и Z", "y? [X] [Z]")

    def execute(self, args):
        if(len(args) < 2):
            raise command.InvalideSyntaxCommandException()
        
        if current_plane == None:
            print("Плоскость не задана. Используйте команду \"setplane\" чтобы задать плоскость")
            return
        
        x, z = list(map(float, args))
        try:
            print(f"Y = {current_plane.find_y(x, z):.2f}")
        except ValueError as e:
            print(e)

class FindZCommand(command.Command):
    def __init__(self):
        super().__init__("z?", "найти координату Z точки, лежащей в плоскости, по известным координатам X и Y", "z? [X] [Y]")

    def execute(self, args):
        if(len(args) < 2):
            raise command.InvalideSyntaxCommandException()
        
        if current_plane == None:
            print("Плоскость не задана. Используйте команду \"setplane\" чтобы задать плоскость")
            return
        
        x, y = list(map(float, args))
        try:
            print(f"Z = {current_plane.find_z(x, y):.2f}")
        except ValueError as e:
            print(e)


command.register(HelpCommand())
command.register(SetPlaneCommand())
command.register(PlaneCommand())
command.register(FindXCommand())
command.register(FindYCommand())
command.register(FindZCommand())

if __name__ == "__main__":
    print(f"Версия программы: {VERSION}")
    print("Воспользуйтесь командой \"help\" для просмотра списка команд")
    while(True):
        command.read()