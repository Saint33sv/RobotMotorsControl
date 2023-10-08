class Engine:
    """Класс двигателя с параметрами мощность, ресурс(изначально 100%) и 
    количество работы выполненой двигателем(абстрактное значение для того чтоб скрипт что то делал)"""

    def __init__(self, max_power: int):
        self.max_power = max_power
        self.moto_resource = 100
        self.useful_action = 0
        self.signal = True

    def exploitation(self, set_power: int) -> bool:
        """Метод експлуатации в зависимости от заданой мощности отнимает мото ресурс двигателя"""
        if set_power <= 0:
            print("Мощность не задана")
            return
        if set_power > self.max_power:
            raise ValueError("Задвнная мощность больше максимальной!")
        if self.moto_resource < 20:
            print("Осталось меньше 20% ресурса двигателя")
            self.signal = False
            return self.signal
        if set_power <= self.max_power/4:
            self.moto_resource -= 0.25
        elif set_power > self.max_power/4 and set_power <= self.max_power/2:
            self.moto_resource -= 0.5
        elif set_power > self.max_power/2 and set_power <= self.max_power-(self.max_power/4):
            self.moto_resource -= 0.75
        else:
            self.moto_resource -= 1
        self.useful_action += set_power/self.moto_resource


class Robot:
    """Класс робота получает мощность в процентах и конвертирует ее исходя из 
    максимальной мощности двигателя. А также записывает данные в бортовой журнал."""

    def __init__(self):
        self.main_engine = Engine(1500)
        self.auxiliary_engine1 = Engine(700)
        self.auxiliary_engine2 = Engine(700)
        self.on = True
        self.off = False

    def power_on(self, engine: Engine, power_percentage: int) -> None:
        logbook = {}
        set_power = (engine.max_power/100) * power_percentage
        while engine.signal:
            engine.exploitation(set_power)
            logbook[engine.moto_resource] = engine.useful_action
        print(logbook)


robo = Robot()
robo.power_on(robo.main_engine, 50)
