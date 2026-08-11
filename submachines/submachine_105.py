import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 864) - 809
    _mask = _data(29, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = 'xM#{d`;L2j1tk<TFf6 GJnC8A|7Bbi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
