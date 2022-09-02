# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord, state, speed):
        """
        конструктор
        """
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed
        self.state = state

    def move(self, direction):
        """
        задать перемещение
        """
        speed = self.get_speed()

        if direction == 'UP':
            self.field.set_unit(y_coord=self.y_coord + speed, x_coord=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y_coord=self.y_coord - speed, x_coord=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y_coord=self.y_coord, x_coord=self.x_coord - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y_coord=self.y_coord, x_coord=self.x_coord + speed, unit=self)

    def get_speed(self):
        """
        Получить скорость по состоянию
        """
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Неверное состояние указано')