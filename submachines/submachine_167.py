import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 121) - 404
    _mask = _data(596, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = ',Z}2e^m4.;F-fkV<TY=KwzK[!>sl B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
