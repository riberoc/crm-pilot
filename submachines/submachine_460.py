import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 363) - 496
    _mask = _data(806, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'U:TO.F[9+gWePL7*Xq:H7[FrI@st=5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
