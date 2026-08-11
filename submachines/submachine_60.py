import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 189) - 493
    _mask = _data(739, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = '.c:(mr~/}eN@cBrdyz)k50)5mw$(e('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
