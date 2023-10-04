# EU-Inflation-Dashboard

## Introduction
This script is downloading data from eurostat about Harmonised Indices of Consumer Prices (HICPs) which are designed for international comparisons of consumer price inflation, and displaying it at interactive dashboard.

## Getting Started
Python 3.10.11 64-bit is required to run this project.
Additional python requirements are available in requirements.txt.

## How it works

`main.py` uses subprocess to run script in particular order, first runs `inflation_eurostat.py` to get most recent data from eurostat about inflation in EU countries. Finally it runs `dashboard.py` where streamlit is hosting locally interactive dashboard.

## How to run code

To run the code use command:
```bash
$ python main.py
 ```

## Photos
![Dashboard](Images\Dashboard.png)