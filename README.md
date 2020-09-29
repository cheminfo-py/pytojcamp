# PyToJCAMP

Python to JCAMP converter. Inspired by [PyToJCAMP](https://github.com/cheminfo/convert-to-jcamp).

Some tools work well with the [JCAMP](http://jcamp-dx.org/) format.
This package allows to convert Python datastructures to JCAMP, this can make it easier for Python based webservices to interact with the [ELN](eln.epfl.ch).

## Installation

To get the latest development version from the head use

```
pip install git+
```

to install the latest stable release use

```
pip install pytojcamp
```

## Usage

See the example notebooks, which you can try out on Binder.

### x/y data

For simple x/y data you can use

```python
from pytojcamp import from_xy
jcamp_string = from_xy((x,y))
```

## n-tuples

To be implemented.
s
