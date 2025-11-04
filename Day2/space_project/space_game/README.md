# Folder structure:
https://github.com/krother/advanced_python/tree/master/solutions/space_game_with_classes

myproject/
    dist/ (build, automatically generated)
    .venv/ (virtual environment: tool that helps you to keep different versions of libraries, contains a Python interpreter and site-packages for this project)
    space_game/ -> this is the name of the Python package that you would import
        __init__.py (optional, useful for managing public API)
        planets.py
        main.py
        text.py
    tests/
        test_space_game.py
    README.md
    pyproject.toml (or setup.py) - configuration for the entire python package

    How to setup a project structure>
    https://www.academis.eu/advanced_python/python_package/README.html 