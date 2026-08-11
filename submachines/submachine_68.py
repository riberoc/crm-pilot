import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 769) - 827
    _mask = _data(105, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = 'Ns! mh#cN*eYn:3*T(Hp;wWL5Mg5Qv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
