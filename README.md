# NEXTPRIME

**Project #5 of the 100 Python Projects Series**

Live Preview: [https://nextprime.onrender.com](https://nextprime.onrender.com)

GitHub Repository: [https://github.com/nishchup489-afk/NEXTPRIME](https://github.com/nishchup489-afk/NEXTPRIME)

CLI Source: [https://github.com/nishchup489-afk/NEXTPRIME](https://github.com/nishchup489-afk/NEXTPRIME)

---

## Project Overview

NextPrime is a Python project that generates the next sequence of prime numbers starting from a user‑defined number.

The project demonstrates a clean implementation of prime number detection combined with algorithmic optimization using square‑root reduction.

The goal of this project is to practice:

* algorithm design
* efficient mathematical computation
* CLI interface design
* web deployment using FastAPI

---

## Implementations Included

This project includes multiple interfaces for experimentation and learning:

1. **Raw Python CLI version** – minimal logic implementation
2. **Colorama UI CLI** – styled terminal output
3. **Rich UI CLI** – enhanced terminal formatting
4. **Textual UI** – experimental terminal interface
5. **FastAPI Web Application** – interactive browser interface

Each version demonstrates how the same algorithm can be applied across different interfaces.

---

## Prime Number Theory

A **prime number** is a number greater than 1 that has exactly two divisors:

1
and
itself

Examples:

```
2, 3, 5, 7, 11, 13, 17
```

Non‑prime numbers are called **composite numbers**.

Example:

```
12 = 2 × 2 × 3
```

---

## Core Algorithm

Instead of checking divisibility up to `n`, the algorithm checks only up to `√n`.

This reduces computation significantly.

### Primality Check

```python
def isPrime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True
```

---

## Prime Sequence Generator

The program repeatedly checks numbers starting from the given input and collects primes until the desired count is reached.

```python
def getNextPrime(start, limit):

    primes = []
    number = start

    while len(primes) < limit:

        if isPrime(number):
            primes.append(number)

        number += 1

    return primes
```

---

## Algorithm Flow

```
START
 |
 |-- User enters start number
 |
 |-- User enters limit
 |
 |-- Set current number = start
 |
 |-- Check if number is prime
 |       |
 |       |-- Yes → add to list
 |       |
 |       |-- No → skip
 |
 |-- Increase number
 |
 |-- Repeat until list size = limit
 |
END → display prime sequence
```

---

## Example

Input:

```
Start number: 10
Limit: 5
```

Output:

```
[11, 13, 17, 19, 23]
```

---

## Tech Stack

* Python
* FastAPI
* TailwindCSS
* Poetry (dependency management)
* Render (deployment)

---

## Part of a Larger Journey

This project is part of the **100 Python Projects Series**.

The goal of this series is to progressively build real‑world applications while mastering:

* algorithms
* backend development
* CLI tools
* deployment
* system design

---

## License

Open source for educational purposes.
