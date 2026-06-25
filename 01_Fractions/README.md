# Fraction Class

A simple Fraction implementation built to learn Python dunder methods.

## Goals
- Understand how Python translates operators into method calls
- Build a mathematical object from scratch

## Features

- Automatic fraction simplification using `gcd`
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Equality (`==`)
- Comparisons (`<`, `>`, `<=`, `>=`)
- Float conversion

## Dunder Methods Used

- `__init__`
- `__repr__`
- `__add__`
- `__sub__`
- `__mul__`
- `__truediv__`
- `__eq__`
- `__lt__`
- `__gt__`
- `__le__`
- `__ge__`
- `__float__`

## Example

```python
a = Fraction(1, 3)
b = Fraction(2, 4)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

## Key Learnings

- Objects store state using `self`
- Constructors enforce invariants
- Operators call dunder methods
- Methods can return new objects
- Mathematical abstractions can be modeled as Python classes

## Next Steps

This project is part of a larger learning journey:

1. Fraction
2. Vector
3. Matrix
4. Tiny Database
5. Tiny Tensor
6. Tiny Autograd
7. FactorTensor
