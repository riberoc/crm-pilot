import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 553) - 381
    _mask = _data(994, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = 'J+Po1!jp{4U IUa3holB1}prTja`*R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
