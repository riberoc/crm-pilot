import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 547) - 691
    _mask = _data(248, None)
    _enc = 42
    return _mask, _enc

def run():
    matrix = '_e fg8WkqyQVKm3FYy!juLJcYXDo`9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
