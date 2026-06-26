# Tiny Vector Library

A lightweight implementation of a mathematical vector in pure Python.

This project was built to practice object-oriented programming, Python's data model, magic methods, and fundamental linear algebra operations without relying on external libraries such as NumPy.

---

## Features

- Vector construction
- String representation
- Length and indexing
- Item assignment
- Vector addition
- Vector subtraction
- Scalar multiplication
- Dot product
- Vector magnitude
- Vector normalization
- Distance between vectors
- Cross product (3D vectors)
- Angle between vectors
- Equality comparison
- Membership testing
- Iteration support
- Copying vectors

---

## Example

```python
from vector import Vector

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1 + v2)
print(v1.dot(v2))
print(v1.magnitude())
```

Output

```text
Vector([5, 7, 9])
32
3.7416573867739413
```

---

## Supported Operations

| Operation             | Example           |
| --------------------- | ----------------- |
| Construction          | `Vector([1,2,3])` |
| Length                | `len(v)`          |
| Indexing              | `v[0]`            |
| Assignment            | `v[0] = 10`       |
| Addition              | `v1 + v2`         |
| Subtraction           | `v1 - v2`         |
| Scalar Multiplication | `v * 3`, `3 * v`  |
| Dot Product           | `v1.dot(v2)`      |
| Magnitude             | `v.magnitude()`   |
| Normalize             | `v.normalize()`   |
| Distance              | `v1.distance(v2)` |
| Cross Product         | `v1.cross(v2)`    |
| Angle                 | `v1.angle(v2)`    |
| Equality              | `v1 == v2`        |
| Membership            | `2 in v`          |
| Iteration             | `for x in v:`     |
| Copy                  | `v.copy()`        |

---

## Project Structure

```
tiny-vector-library/
│
├── vector.py
├── vector_tests.ipynb
├── README.md
└── LICENSE
```

---

## Concepts Practiced

- Python classes
- Object-oriented programming
- Magic methods
- Operator overloading
- Iterators
- List comprehensions
- Linear algebra fundamentals
- Defensive programming
- Error handling

---

## Future Improvements

- Matrix library
- Vector projection
- Reflection
- Linear interpolation (Lerp)
- Higher-dimensional utilities
- NumPy compatibility
- Type hints
- Unit tests with `pytest`

---

## License

This project is released under the MIT License.
