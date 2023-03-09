#!/usr/bin/python3
import imp
import types


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
