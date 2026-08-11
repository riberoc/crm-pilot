import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 954) - 372
    _mask = _data(544, None)
    _enc = 54
    return _mask, _enc

def run():
    matrix = 'PUDGoQEEOhcuI~x% 1S1OfBj<h^]gG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
