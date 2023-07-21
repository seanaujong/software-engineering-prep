# Pointers

[you will never ask about pointers again after watching this video](https://www.youtube.com/watch?v=2ybLD6_2gKM)

## Stack and Heap Memory

[UIUC CS 225 - A detailed explanation of stack and heap memory](https://courses.engr.illinois.edu/cs225/fa2022/resources/stack-heap/#stack)

## Why Use Pointers in C?

[StackOverflow](https://stackoverflow.com/questions/29423757/why-use-pointers-in-c)

> I'm still wondering why in C you can't simply set something to be another thing using plain variables. A variable itself is a pointer to data, is it not? So why make pointers point to the data in the variable when you can simply use the original variable? Is it to access specific bits (or bytes, I guess) of data within said variable? I'm sure it's logical, however I have never fully grasped the concept and when reading code seeing `*pointers` always throws me off.

### Answer

One common place where pointers are helpful is when you are writing functions. Functions take their arguments 'by value', which means that they get a copy of what is passed in and if a function assigns a new value to one of its arguments that will not affect the caller. This means that you couldn't write a "doubling" function like this:


```
void doubling(int x)
{
    x = x * 2;
}
```

This makes sense because otherwise what would the program do if you called doubling like this:

```
doubling(5);
```

Pointers provide a tool for solving this problem because they let you write functions that take the address of a variable, for example:

```
void doubling_p(int *x)
{
    (*x) = (*x) * 2; 
}
```

The function above takes the address of an integer as its argument. The one line in the function body dereferences that address twice: on the left-hand side of the equal sign we are storing into that address and on the right-hand side we are getting the integer value from that address and then multiply it by 2. The end result is that the value found at that address is now doubled.

As an aside, when we want to call this new function we can't pass in a literal value (e.g. `doubling_p(5)`) as it won't compile because we are not properly giving the function an address. One way to give it an address would look like this:

```
int a = 5;
doubling_p(&a);
```

The end result of this would be that our variable a would contain 10.
