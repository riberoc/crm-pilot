import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 862) - 518
    _mask = _data(416, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = '!.A]S:{HA#VAaCyj!wBQ!x[^u[|C8.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
