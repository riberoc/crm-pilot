import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 517) - 769
    _mask = _data(296, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '5]d }<mk0dT*Z]VJjn]G;NL${WGy[L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
