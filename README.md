# CSV

CSV is a small library of CSV utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but CSV consists of
smaller functions to be used rather than relying on larger packages.

Right now, the only functions include convert a file to rows and to json.

## Personal Note

Dates is only on Github because I reference it in other projects. I don't have any plans 
to maintain this project, but I will update it from time to time. 

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-csv-utilities.git
```

# Usage

Once installed, you can import the main class like so:

    >>> from kelmore_csv import CSVTools as CSV
    >>>
    >>> path_to_csv_file: str = '/home/username/Downloads/some_csv.csv'
    >>>
    >>> CSV.to_rows(path_to_csv_file)       # [['first name', 'last name'], ['kyle', 'elmore']]
    >>> CSV.to_json(path_to_csv_file)       # [{'first name': 'kyle', 'last name': 'elmore'}]
    .
    .
    .

# Documentation

To be updated
