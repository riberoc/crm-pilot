import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 852) - 678
    _mask = _data(416, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = 'adt<?pG30[KVt<&WX$mY9D 1l(-B$K'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
