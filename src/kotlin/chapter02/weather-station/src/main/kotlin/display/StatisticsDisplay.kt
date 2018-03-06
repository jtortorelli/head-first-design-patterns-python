package display

import application.WeatherData
import util.Observer

class StatisticsDisplay(private val weatherData: WeatherData) : Observer, DisplayElement {

    private var maxTemp = Float.MIN_VALUE
    private var minTemp = Float.MAX_VALUE
    private var tempSum = 0f
    private var numReadings = 0

    init {
        weatherData.registerObserver(this)
    }

    override fun update(temperature: Float, humidity: Float, pressure: Float) {
        tempSum += temperature
        numReadings++

        if (temperature > maxTemp) {
            maxTemp = temperature
        }
        if (temperature < minTemp) {
            minTemp = temperature
        }

        display()
    }

    override fun display() {
        println("Avg/Max/Min temperature: ${tempSum / numReadings}/$maxTemp/$minTemp")
    }
}