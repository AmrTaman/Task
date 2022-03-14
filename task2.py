class Person:
    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    def sleep(hours):
        if hours == 7:
            print("Happy")
        elif hours > 7:
            print("Lazy")
        else:
            print("Tired")

    def eat(meals):
        if meals == 3:
            print("100% $healthy")
        elif meals == 2:

            print("75% $healthy")
        elif meals == 1:
            print("50% $healthy")

        else:

            print("Unhealthy")

    def buy(items):
        if items > 0:
            money = money - items * 10


class Employee(Person):
    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(hours):
        if hours == 8:
            print("Happy")
        elif hours > 8:
            print("Tired")
        else:
            print("Lazy")

    def salary(value):
        if value >= 1000:
            print("salary is good ")
        else:
            print("salary is low")

    def healthrate(healthrate):
        if healthrate > 0:
            if healthrate < 100:
                print("health rate is valid")

        else:
            print("health rate is valid")
