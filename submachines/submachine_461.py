import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 779) - 834
    _mask = _data(248, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = ":?Z[qqR7]-/odwm6l^q7R'&lCYIt)2"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
