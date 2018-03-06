class Subject:
    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class WeatherData(Subject):

    def __init__(self):
        self.humidity = None
        self.pressure = None
        self.temperature = None
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def get_temperature(self):
        pass

    def get_humidity(self):
        pass

    def get_pressure(self):
        pass

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class Observer:
    def update(self, temp, humidity, pressure):
        raise NotImplementedError


class DisplayElement:
    def display(self):
        raise NotImplementedError


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.max_temp = 0
        self.min_temp = 200
        self.temp_sum = 0
        self.num_readings = 0

    def update(self, temp, humidity, pressure):
        self.temp_sum += temp
        self.num_readings += 1
        if temp > self.max_temp:
            self.max_temp = temp
        if temp < self.min_temp:
            self.min_temp = temp
        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = {(self.temp_sum / self.num_readings)}/{self.max_temp}/{self.min_temp}")


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.last_pressure = 0
        self.current_pressure = 0

    def update(self, temp, humidity, pressure):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: ")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather")


class ThirdPartyDisplay(Observer, DisplayElement):
    def update(self, temp, humidity, pressure):
        pass

    def display(self):
        pass


wd = WeatherData()
ccd = CurrentConditionsDisplay(wd)
sd = StatisticsDisplay(wd)
fd = ForecastDisplay(wd)

wd.set_measurements(80, 65, 30.4)
wd.set_measurements(82, 70, 29.2)
wd.set_measurements(78, 90, 29.2)
