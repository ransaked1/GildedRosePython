# GildedRosePython
This project is my take on [Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata) refactoring kata by Emily Bache. You can find a detailed overview of this project in a two part guide on my [blog](https://codenoodles.com/the-basics-of-writing-quality-unit-tests-with-code-katas/). I did it in Python and the least amount of time and detail possible by writing the tests and refactoring only the code order/some logic.

## Getting Started
Clone the repository and install the prerequisites.

### Prerequisites

Make sure you have python installed:
```
sudo apt-get install python3
```

Install pytest:
```
pip3 install pytest
```

Install coverage:
```
pip3 install coverage
```

## Usage

### Running the program tests
Run the program:
```
python3 test_gilded_rose.py
```

### Running the program with output for 2 days
```
python3 texttest_fixture.py
```

### Test the coverage

Run the program:
```
python3 test_gilded_rose.py
```

Change every “self.assertEquals” to “self.assertEqual” in test_gilded_rose.py and run coverage:
```
coverage run -m pytest test_gilded_rose.py gilded_rose.py
```

Check the coverage report:
```
coverage report -m --include=gilded_rose.py
```

## Built With
* [Pytest 6.2.2] (https://docs.pytest.org/en/stable)
* [Coverage 5.4] (https://coverage.readthedocs.io)
