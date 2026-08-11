import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 231) - 825
    _mask = _data(1234, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = '[k,n3$_5wv*|dU-#fKc~qJ2h9!W}N}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
