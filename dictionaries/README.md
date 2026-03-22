# 📂 Dictionaries – Python Practice Programs

This folder contains Python programs that demonstrate how to use **dictionaries** for storing, updating, and analyzing data. These scripts focus on real-world use cases such as frequency counting, data merging, and identifying maximum values.

Dictionaries are one of the most important data structures in Python because they provide fast key-based lookup and are widely used in text processing, data analysis, and configuration handling.

---

## 🧠 Concepts Covered

* Creating and updating dictionaries
* Iterating through keys and values
* Frequency counting patterns using `dict.get()`
* Merging dictionaries
* Finding maximum values using `max(..., key=...)`
* Handling user input and validation

---

## 📁 Programs Included

### 1. **char_frequency.py**

Counts how many times each character appears in a user-provided sentence.

**Features:**

* Case-insensitive counting
* Supports letters, digits, spaces, and symbols

**Example:**

```
Input:  Hello World
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

**Concepts used:**

* String iteration
* Dictionary frequency counting
* `dict.get()` usage

---

### 2. **word_frequency_counter.py**

Counts the frequency of each word in a sentence.

**Example:**

```
Input:  Python is fun and python is powerful
Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
```

**Concepts used:**

* Tokenizing strings using `.split()`
* Case normalization
* Dictionary aggregation

---

### 3. **merge_two_dicts.py**

Demonstrates how to merge two dictionaries into one using Python’s dictionary methods.

**Example:**

```
{'alex': 23, 'box': 21}
{'ram': 11, 'riya': 1}

Merged Output:
{'alex': 23, 'box': 21, 'ram': 11, 'riya': 1}
```

**Concepts used:**

* `dict.update()`
* Dictionary merging strategies

---

### 4. **student_topper.py**

Stores student names and marks in a dictionary and identifies the student with the highest marks.

**Example:**

```
Alex: 80
Bob: 95
Riya: 90

Output:
Bob is the topper with 95 marks.
```

**Concepts used:**

* Dictionaries for structured data
* `max(dictionary, key=dictionary.get)`
* Input validation

---

## ▶️ How to Run Programs

Navigate to this folder and run any file:

```bash
python char_frequency.py
```

---

## 🎯 Learning Objectives

These programs are designed to strengthen understanding of:

* Mapping data using key-value pairs
* Counting and aggregating information
* Writing reusable dictionary-based functions
* Solving practical problems using Python data structures

---

## 🧑‍💻 Folder Progression

This folder builds a logical learning sequence:

```
Character Frequency → Word Frequency → Dictionary Merging → Data Analysis (Topper)
```

This progression helps move from basic dictionary operations to real-world data processing tasks.

---

## 🚀 Possible Extensions

Future programs that can be added:

* Sorting dictionary by values
* Inverting key-value pairs
* Grouping words by length
* Finding average marks from student data
