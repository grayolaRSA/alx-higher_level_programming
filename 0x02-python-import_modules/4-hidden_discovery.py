#!/usr/bin/python3
import imp
import types


if __name__ == "__main__":
    hidden_4 = imp.load_compiled("hidden_4", "hidden_4.pyc")
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
