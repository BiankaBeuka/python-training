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

uv add ruff
uv run ruff check .\main.py
ruff - complains about the things can be bugs, eg. unused imports, or something else

uv add pylint
uv run pylint .\main.py

main.py:35:9: W0511: TODO: move puzzles to separate functions (fixme)
main.py:79:13: W0511: TODO: use Planet.show_connections instead (fixme)
main.py:82:13: W0511: TODO: add input validation (fixme)
main.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
main.py:16:22: W0622: Redefining built-in 'credits' (redefined-builtin)
main.py:76:16: C0103: Variable name "d" doesn't conform to snake_case naming style (invalid-name)
main.py:11:0: R0912: Too many branches (21/12) (too-many-branches)
main.py:11:0: R0915: Too many statements (53/50) (too-many-statements)

-----------------------------------
Your code has been rated at 8.57/10
