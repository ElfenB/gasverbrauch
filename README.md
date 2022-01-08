# Gas and temperature correlation

This is a small tool to calculate the correlation between gas use and average temperature outside.

It is written in Python and uses only few libraries.

## Installation

0. Set up a virtual environment (recommended)
1. Install libraries from requirements.txt file
2. Create correct CSV-file
3. Execute main.py

## Prerequisites

You will need a CSV file as such:

| verbrauch | temperatur  |
|-----------|-------------|
| 12.228    | 3.850451389 |
| 12.516    | 3.657326389 |
| 15.117    | 2.779375    |
| [...]     | [...]       |

## Result

The result will be a nicely plotted graph with all the calculated information on it.
