package duck

import behavior.FlyNoWay
import behavior.Quack

class ModelDuck: Duck(
        flyBehavior = FlyNoWay(),
        quackBehavior = Quack()
) {
    override fun display() {
        println("I'm a model duck.")
    }

}
