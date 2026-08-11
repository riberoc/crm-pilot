import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 431) - 384
    _mask = _data(97, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = '0Y! K(9*kJLq<i@U,Arq0RZZP86).O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
