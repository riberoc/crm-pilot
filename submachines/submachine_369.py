import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 179) - 446
    _mask = _data(719, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = '^>!5UBJQzQh2Q5iZ*d&n60mhNOqr0&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
