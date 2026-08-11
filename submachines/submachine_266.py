import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 143) - 732
    _mask = _data(846, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = 'poVX-+~A&zZw9mXA$$[C k?e:A9b*_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
