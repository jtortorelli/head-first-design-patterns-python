package duck

import behavior.FlyWithWings
import behavior.Quack

class MallardDuck: Duck(
        flyBehavior = FlyWithWings(),
        quackBehavior = Quack()
) {
    override fun display() {
        println("I'm a real Mallard duck.")
    }
}