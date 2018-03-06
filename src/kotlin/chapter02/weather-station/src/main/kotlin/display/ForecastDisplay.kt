package display

import application.WeatherData
import util.Observer

class ForecastDisplay(private val weatherData: WeatherData): Observer, DisplayElement {

    private var currentPressure = 0f
    private var lastPressure = 0f

    init {
        weatherData.registerObserver(this)
    }

    override fun update(temperature: Float, humidity: Float, pressure: Float) {
        lastPressure = currentPressure
        currentPressure = pressure

        display()
    }

    override fun display() {
        println("Forecast: ${getWeatherMessage()}")
    }

    private fun getWeatherMessage(): String {
        return when {
            currentPressure > lastPressure -> "Improving weather on the way!"
            currentPressure < lastPressure -> "Watch out for cooler, rainy weather."
            else -> "More of the same."
        }
    }
}