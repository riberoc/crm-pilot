import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 797) - 811
    _mask = _data(123, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = '_G[I:EXRqK$T`h`(K.~Y]XS8pYCk L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
