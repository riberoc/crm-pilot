import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 425) - 853
    _mask = _data(529, None)
    _enc = 97
    return _mask, _enc

def run():
    matrix = 'PK NN#M5r17}9DI7-W<+F[js5OZXqs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
