class Car():
    def __init__(self, model, color, intial_speed = 0) -> None:
        self.model = model
        self.color = color
        if intial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = intial_speed

    def speed_up(self):
        self.__speed += 5
    
    def speed_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5
        
    def show_speed(self):
        print("current speed", self.__speed)

car_ops = Car("BMW","BLUE", -100)
car_ops.speed = 15
car_ops.speed_up()
car_ops.show_speed()
