# Data Processing Lab

## Lab Overview
This lab processes data about European cities and countries stored in CSV files. It started as procedural code and was refactored into an object-oriented design. The program can filter rows, aggregate values (average, min, max, count), and join two tables on a common key (`country`). Tables are kept in a simple database (`DB`) where they can be inserted and searched by name.

## Project Structure
```
data-processing-lab/
│
├── README.md              # This file
├── Cities.csv             # Dataset of cities (city, country, latitude, longitude, temperature)
├── Countries.csv          # Dataset of countries (country, population, EU, coastline)
└── data_processing.py     # The classes and the test code
```

## Design Overview

### DataLoader
Loads CSV files.
- **Attributes**
  - `base_path` – folder where the data files are stored (defaults to the folder of the script)
- **Methods**
  - `load_csv(filename)` – reads a CSV file and returns a list of dictionaries (one per row)

### DB
A simple database that holds tables.
- **Attributes**
  - `database` – list of `Table` objects
- **Methods**
  - `insert(table)` – adds a `Table` to the database
  - `search(table_name)` – returns the `Table` with that name, or `None` if it is not found

### Table
Stores one table and provides operations on it.
- **Attributes**
  - `table_name` – name of the table
  - `table` – list of dictionaries (the rows)
- **Methods**
  - `filter(condition)` – returns a new `Table` with only the rows where `condition(row)` is True
  - `aggregate(function, key)` – collects the values of `key` (converted to float when possible) and returns `function(values)`
  - `join(other_table, common_key)` – returns a new `Table` where each row combines a row from this table and a row from `other_table` that have the same value for `common_key`
  - `__str__()` – returns the table name and its rows as a string

## How to Test and Run
1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:
   ```
   python3 data_processing.py
   ```
4. The test code at the bottom of `data_processing.py` runs automatically. Check that the output matches:
   - Average temperature for all cities in Italy: 13.474666666666668
   - Number of countries that have coastline: 29
   - Each row of the joined table contains city, country, latitude, longitude, temperature, population, EU and coastline
   - Cities below 5.0 in non-EU countries: Bergen, Bodo, Orsha, Oslo, Trondheim
   - EU countries without coastline: Min temp 4.54, Max temp 10.34
