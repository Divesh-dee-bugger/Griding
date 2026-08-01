# 🧩 Griding

A lightweight Python module for working with **2D grid-based data structures** using an intuitive **(x, y) coordinate system**.

---

## 🚀 What is Griding?

**Griding** is a simple yet powerful module designed to help you:

- Create and manage 2D grids
- Work with coordinates like a real plane (x, y)
- Build grid-based applications (games, simulations, CLI tools)
- Understand how table-like systems work internally

---

## 🎯 Who is this for?

This package is especially useful for:

- 🧠 Beginners learning data structures
- 🎮 Developers building grid-based games (Tic-Tac-Toe, Battleship, etc.)
- 🧪 People experimenting with 2D data systems
- 🖥️ CLI tool developers who need table-like structures

> ⚠️ Note: This is not a replacement for databases or Pandas. It is designed for learning, prototyping, and lightweight use cases.

---

## 📦 Installation

```bash
pip install Griding
```

---

## 🛠️ Creating a Grid

```python
from Griding.grid import Grid

grid = Grid(4, 3)  # (x, y) → 4 columns, 3 rows
```

---

## 🧭 Coordinate System

Griding uses:

```
(x, y)
```

- x → horizontal (columns)
- y → vertical (rows)

Internally:
```python
grid[y-1][x-1]
```

---

## 🔧 Functions (Detailed Usage)

### ➕ addVal(x, y, value)

Adds a value to a cell.

```python
grid.addVal(1, 1, "Divesh")
```

---

### 🔄 changeVal(x, y, value)

Changes an existing value.

```python
grid.changeVal(1, 1, "DJ")
```

---

### ❌ remVal(x, y)

Removes a value from a cell.

```python
grid.remVal(1, 1)
```

---

### 🔍 getVal(x, y)

Returns value at given coordinate.

```python
val = grid.getVal(2, 3)
```

---

### 📄 getRow(y)

Returns a full row as a list.

```python
row = grid.getRow(2)
```

---

### 📊 getCol(x)

Returns a full column as a list.

```python
col = grid.getCol(3)
```

---

### 🔎 findVal(value)

Finds all occurrences of a value.

```python
positions = grid.findVal("Divesh")
```

Returns:
```
[(x1, y1), (x2, y2), ...]
```

---

### 🧹 clear()

Clears the entire grid.

```python
grid.clear()
```

---

### 🧾 printGrid()

Displays the grid in a clean tabular format.

```python
grid.printGrid()
```

---

### ➖ addLine(row)

Adds a visual separator after a given row.

```python
grid.addLine(1)
```

---

## 💡 Example

```python
grid = Grid(3, 3)

grid.addVal(1, 1, "X")
grid.addVal(2, 2, "O")
grid.addVal(3, 3, "X")

grid.addLine(1)

grid.printGrid()
```

---

## 🔥 Features

- Clean (x, y) coordinate system
- Dynamic column width formatting
- Table-like output
- Value search
- Row & column extraction
- Visual separators

---

## ⚠️ Limitations

- Not optimized for large datasets
- No persistence (in-memory only)
- No relational features
- No advanced querying

---

## 🤝 Contributing

Feel free to fork and improve this project.

---
