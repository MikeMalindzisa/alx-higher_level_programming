#!/usr/bin/python3
import ast


def check_for_imports():
    with open('1-my_list.py', 'r') as file:
        code = file.read()
    tree = ast.parse(code)
    has_imports = any(isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom) for node in ast.walk(tree))
    return has_imports
