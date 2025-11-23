# parameters

- Parameters are the placeholders in the function's definition

### Positional or Normal Parameter

These are the most common type of parameters. The function matches arguments to these parameters based on their **position** in the function call. The number and order of the arguments must exactly match the parameters defined.

**Example 1:**

```python
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# The arguments 'hamster' and 'harry' are assigned by position
# to the parameters 'animal_type' and 'pet_name'.
describe_pet('hamster', 'harry')
```

**Example 2:**

```python
def make_shirt(size, message):
    """Summarizes the shirt that's going to be made."""
    print(f"\nI'm making a {size} t-shirt.")
    print(f'It will have the message, "{message}".')

# The arguments 'large' and 'I love Python' are passed positionally.
make_shirt('large', 'I love Python')
```

-----

### Default Parameter

A default parameter has a default value specified in the function definition. If an argument is provided for it during the function call, the default value is overridden. If no argument is provided, the default value is used.

**Example 1:**

```python
def make_shirt(size='large', message='I love Python'):
    """Summarizes the shirt that's going to be made."""
    print(f"\nI'm making a {size} t-shirt.")
    print(f'It will have the message, "{message}".')

# Uses the default values for both parameters.
make_shirt()

# Overrides the size, but uses the default message.
make_shirt(size='medium')
```

**Example 2:**

```python
def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Uses the default value 'dog' for the animal_type.
describe_pet('willie')

# Overrides the default value for animal_type.
describe_pet(pet_name='harry', animal_type='hamster')
```

-----

### Arbitrary Arguments

These parameters allow a function to accept a variable number of arguments. Python provides two types:

  * **`*args` (arbitrary positional arguments):** This collects any number of non-keyword arguments into a **tuple**.
  * **`**kwargs` (arbitrary keyword arguments):** This collects any number of keyword arguments into a **dictionary**.

**Example 1 (`*args`):**

```python
def make_pizza(*toppings):
    """Prints the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# The function can handle any number of toppings.
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

**Example 2 (`**kwargs`):**

```python
def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# The function gathers all keyword arguments into a dictionary.
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```
