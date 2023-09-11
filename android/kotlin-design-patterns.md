# Kotlin Design Patterns

Kotlin:

- brings the familiarity of statically-typed languages
- brings a vast amount of features aimed at solving real-world problems

The goals of the Kotlin language are to be:

- pragmatic: makes things we do often easy to achieve
- readable: concise and clarified
- easy to reuse
- safe: hard to write code that crashes
- interoperable: allows the use of existing libraries and frameworks

Design patterns are just a proven way to solve a common problem. The basic steps of the design process are:

1. Define exactly what the current problem is
2. Consider different alternatives, based on pros and cons
3. Choose the solution that solves the problem while best fitting your specific constraints

# Creational Patterns

Creational patterns deal with how and when you create your objects. Mastering these design patterns will allow you to manage your objects better, adapt well to changes, and write code that is easy to maintain

- A `Singleton` is the one and only global `object` of a class
- A `Factory` helps us create similar objects
- A `Static Factory` is an alternative to constructors when you want to give each of your constructors a name
    - `Long.valueOf("1")` where `valueOf` is defined in `Long`'s `companion object`
- An `Abstract Factory` is a factory that makes similar factories 
    - `java.util.Collections` is an abstract factory for collections (`emptyMap`, `emptyList`, `emptySet`)
- `Builders` help us create objects with lots of parameters
    - Not as necessary thanks to named and default arguments in constructors
- `Prototypes` let you clone an object easily
    - Data classes have a `.copy()` method that also lets you modify the clone

# Structural Patterns

Structural patterns deal with relationships between objects. These patterns help us extend the functionality of our objects without producing complex class hierarchies.

- A `Decorator` helps us create a set of classes with slightly different behavior.
- An `Adapter` helps us convert one interface to another interface
- `Bridge`
- `Composite`
- `Facade`
- `Flyweight`
- `Proxy`
