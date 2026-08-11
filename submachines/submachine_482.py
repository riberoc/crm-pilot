import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 386) - 665
    _mask = _data(761, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = '[6XEQVP-j[<EeQy/U~:UO,T D5jE`4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
