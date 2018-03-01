package application

import display.CurrentConditionsDisplay
import display.ForecastDisplay
import display.HeatIndexDisplay
import display.StatisticsDisplay

fun main(args: Array<String>) {
    val weatherData = WeatherData()

    val currentConditionsDisplay = CurrentConditionsDisplay(weatherData)
    val statisticsDisplay = StatisticsDisplay(weatherData)
    val forecastDisplay = ForecastDisplay(weatherData)
    val heatIndexDisplay = HeatIndexDisplay(weatherData)

    weatherData.setMeasurements(80f, 65f, 30.4f)
    println()
    weatherData.setMeasurements(82f, 70f, 29.2f)
    println()
    weatherData.setMeasurements(78f, 90f, 29.2f)
}