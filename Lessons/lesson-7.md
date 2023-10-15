# Understanding *args and **kwargs

ACS 1710 - Module 1: Lesson 7

## Learning Outcomes 💫

By the end of this lesson, you should be able to...

- Call a function using named parameters in order to pass in parameters out-of-order.
- Write a function that takes in *args in order to accept any number of arguments.
- Write a function that takes in **kwargs to accept any number of keyword arguments.

## Why this is important

In the next module, you will be using keyword arguments to pass in data to a template. So, it's good to get a refresher on how to use them.

## Videos 🎥

Vid 1 - Named Parameters

https://youtu.be/YLIiqiMmx6Q

Vid 2 - `*args`

https://youtu.be/1E7DyY2hWmM

Vid 3 - **kwargs (keyword arguments)

https://youtu.be/SZTz33iOq00

## Exercises 💪

Answer the questions in Module 1 Section 6 on [Gradescope](http://gradescope.com).

# Written Companion 🗒

<aside>
🤔 What happens if we don't know the number of arguments a function will need - that is, our function needs to accept any number of arguments, and in any order?

</aside>

Using Named Parameters

```python
# a simple Python function with standard arguments
def divide(numerator, denominator):
   return numerator / denominator

answer = divide(12, 3)
print(answer) # prints 4
```

In the above example, the `divide()` function has two parameters: `numerator` and `denominator`.

But, what if we want to pass in these parameters in the reverse order - `denominator` and then `numerator`?

<aside>
💡 We can *label* the parameters we pass in inside of the function's call! This allows us to pass in values out-of-order and ensure that each parameter gets its needed value.

</aside>

```python
# calling the same function with named parameters
def divide(numerator, denominator):
   return numerator / denominator

# this call directly assigns `num2` and `num1` values
answer = divide(denominator=3, numerator=12)
print(answer) # prints 4
```

*Fig 2 - calling a function with named parameters*

- *Note: the order in which arguments are passed doesn't matter if the parameter gets named in the call!*

### Working with `*args`

Now we've seen how to pass in arguments out of order - but what if we want to pass in *any number* of arguments?

```python
# a Python function using *args
def add_all(*args):
  total = 0
  for num in args:
    total += num
  return total

answer = add_all(1, 2, 3, 4, 5)
print(answer) # prints 15
```

In the above example, the add_all function accepts a parameter called *args. The * denotes that args is actually a list that contains all of the passed-in arguments. 

This parameter doesn't need to be called *args! Let's look at another example.

```python
# another Python function using *args
def print_favorite_fruits(*fruits):
  print('Your favorite fruits are:')
  for fruit in fruits:
    print(fruit)

print_favorite_fruits('apple', 'banana', 'kiwi', 'mango')

"""
output:
Your favorite fruits are:
apple
banana
kiwi
mango
"""
```

### Working with `**kwargs`

<aside>
💡 We will be using `**kwargs` in the `templating` lesson, so for more concrete examples with Flask you can look there!

</aside>

`*args` allows us to create functions that accept *any number* of arguments.

`**kwargs` on the other hand, allows us to create functions that accept any number of *labeled* arguments.

When a parameter gets assigned the `**` syntax during a function's definition, the compiler will take all given arguments supplied to it during a function call and load them into a dictionary.

```python
# data will be an array of all the parameters 
# given to it when example() called!
def example(**data):
    print("\nData type of argument:",type(data))

		# since data is an array, it can be iterated through to handle 
		# all given parameters!
    for key, value in data.items():
        print(f"{key} is {value}")

print("--example 1--")
example(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)

print("--example 2--")
example(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


"""
output:

--example 1--
Data type of argument: <class 'dict'>
Firstname is Sita
Lastname is Sharma
Age is 22
Phone is 1234567890

--example 2--
Data type of argument: <class 'dict'>
Firstname is John
Lastname is Wood
Email is johnwood@nomail.com
Country is Wakanda
Age is 25
Phone is 9876543210
"""
```

Since we do not know how much data a user might be submitting, **kwargs will often be employed to ensure that everything gets processed!


