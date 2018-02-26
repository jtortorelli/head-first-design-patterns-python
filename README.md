# Design Patterns
Collection of the code examples from _Head First Design Patterns_ (2004), translated to different languages.

* Chapter 1 - Strategy Pattern
  * SimUDuck
  * Adventure Game
* Chapter 2 - Observer Pattern
  * Weather Station
* Chapter 3 - Decorator Pattern
* Chapter 4 - Factory Pattern
* Chapter 5 - Singleton Pattern
* Chapter 6 - Command Pattern
* Chapter 7 - Adapter and Façade Patterns
* Chapter 8 - Template Pattern
* Chapter 9 - Iterator and Composite Patterns
* Chapter 10 - State Pattern
* Chapter 11 - Proxy Pattern
* Chapter 12 - Compound Patterns
* Chapter 13
* Appendix - Leftover Patterns

## Python

## Kotlin
### Running the test applications
Each directory under the chapter directory represents a separate Gradle project. An executable .jar file can be built using:
```
// macOS
./gradlew clean build

// Windows
gradle clean build
```

The application can then be run using:
```
// macOS
java -jar ./build/libs/[application-name].jar

// Windows
java -jar .\build\libs\[application-name].jar
```
