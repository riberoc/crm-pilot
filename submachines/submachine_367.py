import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 386) - 843
    _mask = _data(1461, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = ';tJu5NYjKdMN]8Kye}CI<x+bq-0HZo'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
