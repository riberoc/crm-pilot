import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 780) - 138
    _mask = _data(517, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = '*j^Z533eb~`ukr6G{sVX[]3?XZ7xUt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
