# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, feld_1_param, field_2_param, d, fl, cr, points_per_action = 1):
        """Перемещение юнита по полю
        :param field: поле по которому перемещается юнит
        :param feld_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param d: направление перемещения
        :param fl: летит ли юнит
        :param cr: крадется ли юнит
        :param points_per_action: базовый параметр скорости
        """
        # проверка флага летит или крадется
        if fl and cr:
            raise ValueError('Рожденный ползать летать не должен!')

        # условия для направления движения вверх, вниз, влево, вправо при состоянии "летит"
        if fl:
            points_per_action *= 1.2
            if d == 'UP':
                new_y = field_2_param + points_per_action
                new_x = feld_1_param
            elif d == 'DOWN':
                new_y = field_2_param - points_per_action
                new_x = feld_1_param
            elif d == 'LEFT':
                new_y = field_2_param
                new_x = feld_1_param - points_per_action
            elif d == 'RIGHT':
                new_y = field_2_param
                new_x = feld_1_param + points_per_action
        # условия для направления движения вверх, вниз, влево, вправо при состоянии "крадется"
        if cr:
            points_per_action *= 0.5
            if d == 'UP':
                new_y = field_2_param + points_per_action
                new_x = feld_1_param
            elif d == 'DOWN':
                new_y = field_2_param - points_per_action
                new_x = feld_1_param
            elif d == 'LEFT':
                new_y = field_2_param
                new_x = feld_1_param - points_per_action
            elif d == 'RIGHT':
                new_y = field_2_param
                new_x = feld_1_param + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
