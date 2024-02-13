# Python Notes

## The Software Designer Mindset

### VS code extensions

- Docker
- Python -> jupiter, pylance ++

### VS code tips

F2 -> rename variable in all files

#### .code/settings.json

```json
{
    "editor.formatOnSaveMode": "file",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
        "source.fixAll": true
    },
    "python.linting.pylintEnabled": false,
    "python.linting.enabled": true,
    "python.analysis.typeCheckingMode": "strict",
    "python.formatting.provider": "black",
    "vim.smartRelativeLine": true
}
```

### Virtual Environment

#### pyenv

Used to manage python versions and virtual environments

```bash
pyenv install 3.8.5
pyenv virtualenv 3.8.5 myenv
pyenv activate myenv
```

#### venv

```bash
python -m venv myenv
source myenv/bin/activate
```

### How python reads inputs (MRO)

MRO - Method Resolution Order

When a function is used, it read the input from right to left.

```py
#This code runs compute pay from Emplyee because Commission is initialized first, then Employee. (from right to left)
@dataclass
class Salary(Employee, Commission)
    return super().compute_pay()
```

### Types

Mainly a helping tool for the developer.
The compiler can still run the code even if the types are wrong.

Python is Dynamically and Strongly typed (variables can change type, but the type is enforced)

#### Static vs Dynamic

Python is a dynamic language. The type of a variable is determined at runtime.

Static required at compiletime
Dynamic required at runtime

Strong vs Weak
How strictly types are compared

The value has type, not the variable. This means that "hello" is a literal['hello'] of type string, not a variable of type string.

```py
my_var = 5 + "hello" // Not allowed (strictly typed) 
```

#### Hinting

```py
def add_three(x: int) -> int: # x is of type int and the function returns an int 
    return x + 3
```

#### Callables

```py
def add_three(x: int) -> int: # x is of type int and the function returns an int 
    return x + 3

def main()
    my_var = add_three
    print(my_var(5)) # 8 (my_var is a callable) 
```

##### Callables explained

```py
from typing import Callable

IntFunction = Callable[[int], int] # A function that takes an int and returns an int

def add_three(x: int) -> int: # x is of type int and the function returns an int 
    return x + 3

def main()
    my_var: IntFunction = add_three # my_var is a function that takes an int and returns an int
    print(my_var(5)) # 8 (my_var is a callable) 
```

#### Nominal vs Structural Typing

Nominal: Based on the name of the type
Structural: Based on the structure of the type (duck typing)
    "If it looks like a duck and quacks like a duck, it is a duck"

```py
class Dog:
    def bark(self):
        print("Woof")

class Cat: 
    def meow(self):
        print("Meow")
```

```py
class Book:
    def __init__(self, author: str, title:str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int: # This is a duck method. It does now care what the name of the method is, it is called when the len() function is called on the object
        return self.pages

    def main():
      my_str = "hello"
      print(len(my_str)) # 5
      my_list = [34, 53, 235, 23]
      print(len(my_list)) # 4
      my_dict = {"one": 1, "two": 2}
      print(len(my_dict)) # 2
      my_book = Book("John Doe", "A cool book", 300)
      print(len(my_book)) # 300
```

### Slice

```py
my_list = [1, 2, 3, 4, 5]
print(my_list[:]) # [1, 2, 3, 4, 5]
print(my_list[:1]) # [1]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[1:3]) # [2, 3]
print(my_list[::2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 4, 3, 2, 1]
```

### Data structures

Python has not allocated any memory for the variable until it is used. This means that in INT can be stored in 4 bits, 2bytes, 4bytes etc. depending on the size of the number.
The only limit for the size of the data structure is the memory of the computer.
This bloats the memory usage, but makes the language more flexible.

Integers are precise.
Floating points are rounded and un-precise.

#### List

Mutable ordered sequence of indexed elements.
Not as fast as array. Stored several places in memory.

Good for:

- Dynamic size
- Fast insertions and deletions
- Fast appends
- Ordered

Not good for:

- Slow lookups (often lookups)
- Slow deletions
- Slow insertions

```py
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(my_list[:1]) 
```

#### Dictionary

Key-value pairs. Unordered, mutable and indexed.

Good for:

- Fast lookups (hash table)
- Fast insertions
- Fast deletions

Not good for:

- Not ordered
- Takes up more memory than a list

```py
my_dict = {
    "name": "John Doe",
    "age": 34,
    "city": "Oslo"
}

def main():
    print(my_dict["name"]) # John Doe
    print(my_dict.get("name")) # John Doe
    print(my_dict.get("name", "default")) # John Doe
    print(my_dict.get("not_a_key", "default")) # default
    print(my_dict.keys()) # dict_keys(['name', 'age', 'city'])
    print(my_dict.values()) # dict_values(['John Doe', 34, 'Oslo'])
    print(my_dict.items()) # dict_items([('name', 'John Doe'), ('age', 34), ('city', 'Oslo')])
```

#### Strings

Behaves like lists, but are immutable.
No difference between single, double, triple quotes.
No difference between single char, string or list of chars.

```py
def main():
    my_str = "hello"
    my_str = 'hello'
    my_str = """hello"""
    my_str = '''hello'''
    my_str = "hello" + "world"
    my_str = "hello" * 3 # hellohellohello
    my_str = "hello"[0] # h
    my_str = "hello"[-1] # o
    my_str = "hello"[1:3] # el
    my_str = """
    hello
    world
    """ # hello\nworld
    my_str = "hello" in "hello world" # True
    my_str[3] = "p" # Not allowed
    
    print(my_str) # hello
```

#### Formatted strings (f-strings)

```py
def main():
    my_str = "total amount"
    cents: int = 30000
    formatted_str = f"{my_str}  ${cents / 100:.2f}" # total amount $300.00
    print(formatted_str)

```

#### Enums

Limits the allowed values of a variable.
Lets the developer know what values are allowed.

```py
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Mounths(Enum):
    JANUARY = auto()
    FEBRUARY = auto()
    MARCH = auto()

def main():
    my_color = Color.RED
    print(my_color) # Color.RED
    print(my_color.name) # RED
    print(my_color.value) # 1
    print(Mounths.JANUARY) # Mounths.JANUARY
```

#### Tuples

Grouping several values
If the tuple is immutable, the values are hashable and can be used as keys in a dictionary.
Fast to access

If you have a more complex data structure with several values, it is better to use a class.

```py
def birthday_month_year() -> tuple[str, int, int]:
    return "January", 10, 1986

month, day, year = birthday_month_year()
print(month) # January
print(day) # 10
print(year) # 1986

```

#### Sets

Unordered, mutable and no duplicates.
Fast lookups, insertions and deletions.

```py
my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}
my_set.remove(3)
print(my_set) # {1, 2, 4, 5, 6}
```

### Dunder methods

Methods starting and ending with double underscores ('__') are called dunder methods.
Dunder = Double UNDERscore

### Class

Classes are blue-print of objects.

It can have methods, properties, constructors, destructors, etc.

#### Data classes

Classes can also be 'dataclasses', which is a class with only data and methods that operate on the data.
A dataclass does not need a constructor, because it is automatically generated.
Dataclasses are immutable by default. This means that the data cannot be changed after the object is created.
You can also give default values to the dataclass.

Decoratesd with @dataclass

Using field() to give default values to the dataclass is more flexible than using the default value in the constructor.

```py
from dataclasses import dataclass

@dataclass
class Book: 
    author: str
    title: str
    pages: int = 300
    children: list[Book] = field(default_factory=list) # Default value is a list
    parent : list[Book] = field(default_factory=parent_books) # Default value is a list of parent books
    serial_number: int = field(3, init=False) # Not allowed to set the value of the serial number

    def __len__(self) -> int:
        return self.pages
    
    def change_author(self, new_author: str) -> None:
        self.author = new_author
    
    def add_child(self, child: Book) -> None:
        self.children.append(child)
    
    def add_parent(self, parent: Book) -> None:

    def parent_books() -> list[Book]:
        return [Book("John Doe", "A cool book", 300), Book("Jane Doe", "Another cool book", 400)]

def main():
    print(len(Book("John Doe", "A cool book", 300))) # 300
```

##### Read only data class

Not allowed to change the data in the dataclass after it is created.

```py

from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    author: str
    title: str
    pages: int = 300


def main():
    my_book = Book("John Doe", "A cool book", 300)
    my_book.author = "Jane Doe" # Not allowed
```

#### Functions

Functions and properties are inherited from the parent class.

Pure functions are functions that do not change the state of the object. It always returns the same value for the same input.

Side-effect functions change the state of the object.
It can also change the state of other objects.

- Should be avoided if possible
- Makes the code harder to understand
- Makes the code harder to test
- Makes the code harder to maintain

**Always think about if you are creating a pure or side-effect function.**
Always think about if you are creating a pure or side-effect function.
If you are creating a side-effect function, think about if it is possible to create a pure function instead.

#### Callable dunder method

Use the **call** method to make an object callable.
calling the object will call the **call** method.

```py
class AddThree:
    def __call__(self, x: int) -> int:
        return x + 3

def main():
    my_var = AddThree() # my_var is now a callable and the return was 0
    print(my_var(5)) # 8
```

#### Higher-order functions

A function that takes a function as an argument or returns a function.

```py
@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion( # Higher-order function
    customer: list[Customer], is_eligible: Callable[[Customer], bool]) -> None:
    for customer in customers:
        if is_eligible(customer):
            print(f"{customer.name} is eligible for the promotion")            
        else:
            print(f"{customer.name} is not eligible for the promotion")
)

def is_eligible_for_promotion(customer: Customer) -> bool: # Pure function
    return customer.age >= 18

def main():
    customers = [
        Customer("John Doe", 34),
        Customer("Jane Doe", 17)
    ]
    send_email_promotion(customers, is_eligible_for_promotion) # Higher-order function called wih a pure function as a parameter

    # Alternative to use lambda function
    send_email_promotion(customers, lambda customer: customer.age >= 18) # Same results as above
```

#### Closure

A function that returns a function.

```py
def add(x: int) -> Callable[[int], int]:
    def inner(y: int) -> int:
        return x + y
    return inner

def main():
    add_three = add(3)
    print(add_three(5)) # 8
```

#### Partial function applications

A function that returns a function with some of the arguments already set.

```py
from functools import partial

def add(x: int, y: int) -> int:
    return x + y

def main():
    add_seven = partial(add, 7) # add_seven is now a function that takes one argument, but it's initialized with 7
    print(add_seven(5)) # 12
```

#### Grouping functions

A class is a way to group functions and data together.
You can create a list, tuple set or dictionary of functions.

```py

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> int:
    return x / y

def main():
    OPERATIONS =  [ # List of functions
        add,
        subtract,
        multiply,
        divide
    ]
    for operation in OPERATIONS:
        print(operation(5, 3)) # 8, 2, 15, 1.6666666666666667
```

#### Class vs Functions

Use a class if you need to group functions and data together.
Use a function if you only need to perform a single operation.

In general, if you have lots of instance variables and methods that operate on the instance variables, use a class.
If you only have a few instance variables and methods that operate on the instance variables, use a function.

### Inheritance

#### ABC (Abstract Base Class)

The super class is the parent class. It could be defined as a class, but to prevent it from beeing instantiated, it is defined as an abstract class.

The sub class is the child class that implements the super class.

```py
from abc import ABC, abstractmethod

class Animal(ABC): # Super class. Serves as an interface (ABC = Abstract Base Class)
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> None:
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal): # Sub class inherits from Animal
    def speak(self) -> None:
        print(f"{self.name} says woof")

class Cat(Animal): # Sub class inherits from Animal
    def speak(self) -> None:
        print(f"{self.name} says meow")

def pat_animal(animal: Animal) -> None:
    print(f"Patting {animal.name}")
    print(f"The animal responds happily: {animal.speak()}")

def main():
    my_dog = Dog("Rex")
    my_dog.speak() # Rex says woof
    my_cat = Cat("Whiskers")
    my_cat.speak() # Whiskers says meow
    my_animal = Animal(my_dog) # Not allowed
```

#### Protocols

A protocol is a class that only contains abstract methods.
It is used to define the interface of a class.
Protocols do not require that you define a relationship between the sub class and the super class. The relationship between classes are established when the class that requires the inheritance is called.

By using protocols you can create smaller interfaces that not all classes need to implement.

```py
from typing implement Protocol

class Animal(Protocol): # Protocol
    name: str
    def speak(self) -> None:
        ... # standard way of defining a protocol

class Talking(Protocol): # Protocol
    def speak(self) -> None:
        ... # standard way of defining a protocol 

class PlayFetch(Protocol): # Protocol
    def fetch(self) -> None:
        ... # standard way of defining a protocol

class Dog:
    def __init__(self, name: str) -> None:
        self.name = name
    def speak(self) -> None:
        print("Woof")

    def fetch(self) -> None:
        print("Fetching")

class Cat:
    def __init__(self, name: str) -> None:
        self.name = name

    def silent(self) -> None:
        print("...")

def get_name(animal: Animal) -> None:
    print(f"The animal's name is: {animal.name}")

def pat_animal(Talking: Animal) -> None:
    print(f"The animal responds happily: {animal.speak()}") 

def fetch_stick(PlayFetch: PlayFetch) -> None:
    print(f"The animal fetches the stick: {animal.fetch()}")

def main():
    my_dog = Dog("rex")
    my_dog.speak() # Woof
    my_cat = Cat("Mons")
    pat_animal(my_dog) # Patting Rex\nThe animal responds happily: Woof
    pet_animal(my_cat) # Not allowed (Cat does not implement the Animal protocol)
    play_fetch(my_dog) # Fetching
    play_fetch(my_cat) # Not allowed (Cat does not implement the PlayFetch protocol)
    get_name(my_dog) # The animal's name is: Rex
```

#### Difference between ABC and Protocol

Cleaner way to implement the inheritance.
The relationship between the sub class and the super class is established when the class that requires the inheritance is called.
The protocol does not belong to the sub class, but to the method that requires the calling class expects the sub class to implement.

ABS give ability to define initial values on the super class. This is not possible with protocols.

### The 7 Principles of Modern Software Design

#### Favor Composition over Inheritance

##### Composition

Composition is an object -oriented design concept that models a **has-a** relationship between objects.
A composite class **has-a** component of another class.

```py
class Engine:
    def start(self) -> None:
        print("Engine started")

class Car:
    def __init__(self) -> None:
        self.engine = Engine() # Car has a engine

    def start(self) -> None:
        self.engine.start()

def main():
    my_car = Car()
    my_car.start() # Engine started
```

##### Cohesion (Single Responsibility Principle)

Important to write code with high cohesion!

Cohesion is a measure of how closely the methods of a class are related to each other.

- Does the function / method have only one responsibility, it has high cohesion.
  - Supermarket has "lots of different items"
  - Cheese store has only cheese, but also the best cheese.

Method for improving cohesion:

- Look for methods that are doing more than one thing
- Look for methods that are doing things that are not related to the class
- Look for methods that uses data from other classes
- Split the method into smaller methods
- Move the method to another class

##### Coupling

Coupling is a measure of how much a class is dependent on another class.

###### Content coupling

When a class uses the data of another class.

If a class gets a reference to another class or uses the data of another class, it is content coupling.

###### Global coupling

When a class uses a global variable.
Try to let the class use the global variable as a parameter instead. This makes the class more flexible and easier to test.

###### External coupling

When a class uses a method from another external api

###### Control coupling

When a module or class control the flow of another class/method.

###### Data coupling

When a class uses the data of another class.

###### Stamp coupling

When a class uses the data of another class.

###### Message coupling

Messages are used to communicate between classes.

#### The Law of Demeter (Principle of Least Knowledge)

The Law of Demeter is a design principle that states that a method of an object should only call methods of:

- The object itself
- The method's parameters
- Objects that are created within the method
- Objects that are stored in the object's instance variables

#### Start with the data

Data driven design is a design principle that states that you should start with the data and then create the methods that operate on the data.

Put the data in the center of the design and then create the methods that operate on the data. They should be as close to the data as possible.

Use a layered approach. If your calculations require data from outside your class, create a property that can be used to get the data. This makes the class more flexible and easier to test.

If you need to know about the inner structure of a class, when calling it from the outside, it is a sign that the class is not designed correctly.

#### Depend on abstractions, not concretions

Try to make the classes less dependent on others. Stitch things togheter in the main class.
Use protocols to make the classes less dependent on each other.
If you setup your code well, you will have one place where you deal with dependencies.

#### Separate creation from use

Factory pattern is a way of implementing concepts of separation of creation and use.

With protocols, you can define how an object should look given a certain input.
Helps with OCP (Open Closed principle)

```py
"""
Basic video exporting example
"""

from pathlib import Path
from typing import Protocol


class VideoExporter(Protocol):
    """Basic representation of video exporting codec."""

    def prepare_export(self, video_data: str) -> None:
        """Prepares video data for exporting."""
        raise NotImplementedError

    def do_export(self, folder: Path) -> None:
        """Exports the video data to a folder."""
        raise NotImplementedError


class LosslessVideoExporter:
    """Lossless video exporting codec."""

    def prepare_export(self, video_data: str):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter:
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data: str):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter:
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data: str):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(Protocol):
    """Basic representation of audio exporting codec."""

    def prepare_export(self, audio_data: str):
        """Prepares audio data for exporting."""

    def do_export(self, folder: Path):
        """Exports the audio data to a folder."""


class AACAudioExporter:
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data: str):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter:
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data: str):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class ExporterFactory(Protocol):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    def create_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter belonging to this factory."""

    def create_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter belonging to this factory."""


class FastExporter:
    """Factory aimed at providing a high speed, lower quality export."""

    def create_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter:
    """Factory aimed at providing a slower speed, high quality export."""

    def create_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter:
    """Factory aimed at providing a low speed, master quality export."""

    def create_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


FACTORIES: dict[str, ExporterFactory] = {
    "low": FastExporter(),
    "high": HighQualityExporter(),
    "master": MasterQualityExporter(),
}


def read_factory() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference."""

    while True:
        export_quality = input(
            f"Enter desired output quality ({', '.join(FACTORIES)}): "
        )
        try:
            return FACTORIES[export_quality]
        except KeyError:
            print(f"Unknown output quality option: {export_quality}.")


def do_export(fac: ExporterFactory) -> None:
    """Do a test export using a video and audio exporter."""

    # retrieve the exporters
    video_exporter = fac.create_video_exporter()
    audio_exporter = fac.create_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


def main() -> None:
    # create the factory
    factory = read_factory()

    # perform the exporting job
    do_export(factory)


if __name__ == "__main__":
    main()
```

#### Keep things simple

DRY - Don't repeat yourself // Find code that could be generalized and remove duplications.

KISS - Keep it stupidly simple //

YAGNI - You ain't gonna need it // Don't implement something that you don't need right now

### Mixins

Should not be used.
Multiple inheritance to inject certain behavior into a class.

### Error handling

#### Try Catch

You should only use Try/Catch if you intend to let the application continue in a degraded state or you want to take some special measures.

Create your own error handling class

```py
@dataclass
class NotFoundError(Exception):
    id: str


@dataclass
class NotAuthorizedError(Exception):
    id: str


@dataclass
class Blog:
    id: str
    published: datetime
    title: str
    content: str
    public: bool


def blog_lst_to_json(item: list[Any]) -> Blog:
    return Blog(
        id=item[0],
        published=item[1],
        title=item[2],
        content=item[3],
        public=bool(item[4]),
    )
    # return Blog(*item)


def fetch_blog(blog_id: str):
    try:
        # connect to the database
        con = sqlite3.connect("application.db")
        cur = con.cursor()

        # execute the query and fetch the data
        cur.execute("SELECT * FROM blogs where id=?", [blog_id])
        result = cur.fetchone()

        # return the result or raise an error
        if result is None:
            raise NotFoundError(blog_id)

        blog = blog_lst_to_json(result)
        if not blog.public:
            raise NotAuthorizedError(blog_id)
    finally:
        # close the database
        print("closing the database")
        con.close()

    return blog


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
```

#### Context manager

Context manager is usefull if you want to do a task while a connection is opened, like DB read or file read.

```py

class SQLite:
    def __init__(self, file="application.db"):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        print("Closing the connection")
        if self.conn #Only close if a connection actually was made
            self.conn.close()


def fetch_blog(blog_id: str):
    with SQLite("application.db") as cur:

        # execute the query and fetch the data
        cur.execute("SELECT * FROM blogs where id=?", [blog_id])
        result = cur.fetchone()

        # return the result or raise an error
        if result is None:
            raise NotFoundError(blog_id)

        blog = blog_lst_to_json(result)
        if not blog.public:
            raise NotAuthorizedError(blog_id)
        return blog
```

### Structuring a complex projects

#### Project files

files on root:

- .gitignore

```gitignore
**/*.pyc
.coverage
htmlcov
```

- .pylintrc
- README.md
- requirements

#### Project folders

- .vscode/settings.json
- assets // Files or data needed for program to work (images, pdf's...)
- docs // HTML / md files with documentation for project
- wiki // Contribution and wiki
- locales // language and translation for all ui related parts of the project
- src // This is where your main.py file should live. All packages you create should be under this folder.
- tests // unit-tests
- tools // Scripts for resetting db, tools to cleanup, migrations +++
- vendor // 3.rd party dependencies used by the project

#### Modules and packages

Python considers every file as a module, and every folder as a package.

- A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.
- A package is a folder containing Python files and an **init**.py file.
- The **init**.py file is used to initialize the package.
- The **init**.py file can be empty, but it can also contain code to initialize the package.

#### Absolute and Relative Imports

```py
from package_1.file_1 import function_1 ## This is an absolute import (Use full path to the file)
from .file_1 import function_1 ## This is a relative import
```

#### Multiple packages

Packages can be nested inside each other.
Relative imports are not allowed between packages

#### Import Tips

Watch out for wildcard import (*)

```py
from package_1 import * # Not advised. Makes it unclear where the function comes from
```

```py
from package_1.file_1 import function_1 as f1 # Advised. Makes it clear where the function comes from and f1 is shorter to use
```

#### Naming

- Use snake_case for file names, variable names and function names
- Use CamelCase for class names
- Use UPPERCASE for constants
- Use descriptive names.
- Use the same name for the file and the class in the file. Avoid generic names, be specific.
  - Files like "utils.py" or "helpers.py" are not descriptive enough. Use "file_reader.py" or "file_writer.py" instead. They also tend to room more than they should.

#### Security

Don't put username and password, connection strings or secrets into the source code.

- Use separate config files
- Use environment variables
-
