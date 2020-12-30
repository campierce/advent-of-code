# advent-of-code

My solutions to [Advent of Code](https://adventofcode.com/) in Python 3.

Development environment:

* [Sublime Text 3](https://www.sublimetext.com/3) with [Python Improved](https://packagecontrol.io/packages/Python%20Improved) for syntax highlighting and the following .sublime-settings:
```JSON
{
	"extensions": ["py"],
	"rulers": [79],
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"word_wrap": true,
	"wrap_width": 80
}
```
* Retrieve puzzle inputs via the [aocd](https://github.com/wimglenn/advent-of-code-data) library
* Run programs directly in ST3 with `cmd+b` via the following build system:
```JSON
{
	"cmd": ["python3", "-u", "$file"],
	"selector": "source.python"
}
```
