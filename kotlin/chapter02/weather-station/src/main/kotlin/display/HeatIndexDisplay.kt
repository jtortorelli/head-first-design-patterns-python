package display

import application.WeatherData
import util.Observer
import kotlin.math.exp
import kotlin.math.pow

class HeatIndexDisplay(private val weatherData: WeatherData): Observer, DisplayElement {

    private var heatIndex = 0f

    init {
        weatherData.registerObserver(this)
    }

    override fun update(temperature: Float, humidity: Float, pressure: Float) {
        heatIndex = calculateHeatIndex(temperature, humidity)

        display()
    }

    override fun display() {
        println("Heat index is $heatIndex")
    }

    private fun calculateHeatIndex(temperature: Float, humidity: Float): Float {
        return (16.923 +
                1.85212e-1 * temperature +
                5.37941 * humidity -
                1.00254e-1 * temperature * humidity +
                9.41695e-3 * temperature.pow(2) +
                7.28898e-3 * humidity.pow(2) +
                3.45372e-4 * temperature.pow(2) * humidity -
                8.14971e-4 * temperature * humidity.pow(2) +
                1.02102e-5 * temperature.pow(2) * humidity.pow(2) -
                3.8646e-5 * temperature.pow(3) +
                2.91583e-5 * humidity.pow(3) +
                1.42721e-6 * temperature.pow(3) * humidity +
                1.97483e-7 * temperature * humidity.pow(3) -
                2.18429e-8 * temperature.pow(3) * humidity.pow(2) +
                8.43296e-10 * temperature.pow(2) * humidity.pow(3) -
                4.81975e-11 * temperature.pow(3) * humidity.pow(3)).toFloat()
    }
}