"""
print is one of the built in functions supported by python interpreter.

It's full definition is

def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None: ... 

"""

#Multiple Strings will be printed with 
#   a default separator of space
#   a newline at the end of all the strings
print("Hello","World")