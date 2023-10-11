import time


class Engine:
    """Класс двигателя с параметрами мощность, ресурс(изначально 100%) и 
    количество работы выполненой двигателем(абстрактное значение для того чтоб скрипт что то делал)"""

    def __init__(self, name: str, max_power: int):
        self.name = name
        self.max_power = max_power
        self.moto_resource = 100
        self.useful_action = 0
        self.signal = True
        self.logbook = {}

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
        self.logbook[self.moto_resource] = self.useful_action


class Robot:
    """Класс робота получает мощность в процентах и конвертирует ее исходя из 
    максимальной мощности двигателя. А также записывает данные в бортовой журнал."""

    def __init__(self):
        self.main_engine = Engine("main_en", 1500)
        self.auxiliary_engine1 = Engine("aux_en1", 700)
        self.auxiliary_engine2 = Engine("aux_en2", 700)
        self.on = True
        self.off = False
        self.robot_logbook = {}

    def power_on(self, engine: Engine, power_percentage: int) -> None:
        if not engine.signal:
            return
        logbook = {}
        set_power = (engine.max_power/100) * power_percentage
        engine.exploitation(set_power)
        self.robot_logbook[engine.name] = engine.logbook
        print(f"Engine {engine.name} {power_percentage}% included")

    def robot_work_algorithm(self, work_time_in_sec: int) -> None:
        while work_time_in_sec:
            self.main_engine.signal = True
            for _ in range(4):
                self.power_on(self.main_engine, 50)
                # time.sleep(1)
                work_time_in_sec -= 1
            self.main_engine.signal = False
            self.auxiliary_engine1.signal = True
            self.auxiliary_engine2.signal = True
            for _ in range(3):
                self.power_on(self.auxiliary_engine1, 30)
                self.power_on(self.auxiliary_engine2, 30)
                # time.sleep(1)
                work_time_in_sec -= 1
            self.auxiliary_engine1.signal = False
            self.auxiliary_engine2.signal = False
        else:
            self.auxiliary_engine1.signal = True
            self.auxiliary_engine2.signal = True
            self.main_engine.signal = True
            for _ in range(5):
                self.power_on(self.main_engine, 70)
                self.power_on(self.auxiliary_engine1, 70)
                self.power_on(self.auxiliary_engine2, 70)


robo = Robot()
robo.robot_work_algorithm(21)
print(robo.robot_logbook)
