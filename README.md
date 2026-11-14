# Data Processing Lab

A small Python project that reads a CSV file of European cities and answers simple questions about it (filtering and aggregation). The same tasks are written three times, moving from a simple script to a procedural style and then to an object-oriented style.

## Files

| File | Description |
|---|---|
| `Cities.csv` | Data for 213 cities: `city`, `country`, `latitude`, `longitude`, `temperature` |
| `data_processing.py` | Loads the CSV and prints the results |
| `README.md` | This file |

## How to run

Requires Python 3 (no extra packages). Open a terminal in this folder and run:

```bash
python3 data_processing.py
```

## What the program prints

1. The average temperature of all the cities
2. All cities in Germany
3. All cities in Spain with a temperature above 12°C
4. The number of unique countries
5. The average temperature of all the cities in Germany
6. The max temperature of all the cities in Italy

Expected results:

| Question | Result |
|---|---|
| Average temperature (all cities) | 9.4978 °C |
| Cities in Germany | 14 cities |
| Cities in Spain above 12°C | 13 cities |
| Unique countries | 37 |
| Average temperature in Germany | 7.8693 °C |
| Max temperature in Italy | 17.9 °C |

## Code structure (OOP version)

### `DataLoader`
- `__init__(base_path=None)` – sets the folder to read files from (defaults to the folder of the script)
- `load_csv(filename)` – reads a CSV file and returns a list of dictionaries

### `Table`
- `__init__(table_name, table)` – stores a name and a list of dictionaries
- `filter(condition)` – returns a **new `Table`** with only the rows where `condition(row)` is `True`, so calls can be chained, e.g. `table.filter(...).aggregate(...)`
- `aggregate(function, key)` – collects the values of `key` (converted to `float` when possible) and returns `function(values)`, e.g. `sum`, `max`, or a lambda
- `__str__()` – shows the table name and its rows

Example:

```python
loader = DataLoader()
cities = Table('cities', loader.load_csv('Cities.csv'))

germany_avg = cities.filter(lambda x: x['country'] == 'Germany') \
                    .aggregate(lambda x: sum(x) / len(x), 'temperature')
```

## Commit history

1. **Initial commit** – script version using loops, list comprehensions, `filter` and `lambda`
2. **Procedural refactor** – added `filter_items()` and `aggregate()` functions
3. **OOP refactor** – added `DataLoader` and `Table` classes
