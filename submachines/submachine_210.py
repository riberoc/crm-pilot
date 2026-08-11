import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 554) - 142
    _mask = _data(705, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = ':<V).0bU?BF.{c Z>iPtMuaf5[,e[8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
