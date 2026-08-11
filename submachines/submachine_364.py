import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 401) - 561
    _mask = _data(881, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = '(y;){[(KH4{Mc:-Iu@9M5GruHDY]Xy'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
