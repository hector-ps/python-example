# python-template
Repo to test templates on Python projects

## Layout

Tests are in repository root, at same level of project.

The import statements on the tests are in the form of:

`from myproject.parsing.parser`

You should use `python -m pytest` from the `pytest-layouts` folder
to run the tests. This adds the repo folder to the `syspath` variable.

```
pytest-layouts
├── myproject
│   ├── __init__.py
│   ├── __main__.py
│   ├── parsing
│   │   ├── __init__.py
│   │   └── parser.py
│   └── README.md
└── test
    └── test_parser.py # import of the form
                       # from myproject.parsing.parser import parse_temp
``` 