import logic
import graphics
# The creation of the two players and the field
field = logic.Field()
player_x = logic.Player('X')
player_0 = logic.Player('0')
# 1. крестик начинает первым
# 2. крестик вводит данные
# 3. проверяем данные, которые ввел крестик
# 4. если данные не корресктны, просим игрока ввести данные еще раз
# 5. проверяем есть ли нужная ячейка
# 6. если ячейка занята, просим игрока выбрать другую ячейку
# 7. если ячейка свободна - заполняем ее крестиком
# 8. переход хода к нолику
# 9. повтор действий 2-7 для нолика
# 10. с пятого хода проверяем победителя
# 11. если победитель есть - выводим на экран победителя и заканчиваем игру
# 12. если победителя нету - продожаем игру3. если сделан 9-й ход, а победителя нету - говорим пользователям, что у нас ничья

for i in range(9):
    field.print_field()
    if i % 2 == 0:
        while True:
            data = player_x.move()
            if player_x.data_check(data):
                coordinates = field.convert(data)
                if field.cell_fill(coordinates[0], coordinates[1], player_x):
                    field.cell_fill(coordinates[0], coordinates[1], player_x)
                    break
                else:
                    continue
            else:
                continue

    if i % 2 != 0:
        while True:
            data = player_0.move()
            if player_0.data_check(data):
                coordinates = tuple(field.convert(data))
                if field.cell_fill(coordinates[0], coordinates[1], player_0):
                    field.cell_fill(coordinates[0], coordinates[1], player_0)
                    break
                else:
                    continue
            else:
                continue

    if i >= 4:
        if field.winner(player_x):
            print('player:x have won')
            break

        if field.winner(player_0):
            print('player_0 have won')
            break

    if i == 8:
        print('Tie')
print('End of the game')

