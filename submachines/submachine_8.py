import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 223) - 115
    _mask = _data(43, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = 'de6E{U:A8DaKW5C%!|[T:y*B(N#/(r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
