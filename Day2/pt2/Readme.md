Code checks

https://www.academis.eu/advanced_python/quality/code_checks.html

uv init
uv add mypy
uv run mypy .\type_annotations.py
--  
""
type_annotations.py:19: error: Dict entry 3 has incompatible type "Literal['watermelon']": "float"; expected "Literal['apple', 'pear', 'cantaloupe']": "float"  [dict-item]
Found 1 error in 1 file (checked 1 source file) 
""

mypy is a nice tool to run checks on the types

trainingPy\Day2\pt2> uv run mypy --strict .\type_annotations.py
Success: no issues found in 1 source file

uv add black
uv run black type_annotations.py
    All done! ✨ 🍰 ✨
    1 file reformatted.

uv add isort
uv run isort space_game.py // sorts the imports