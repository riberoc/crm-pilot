import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 691) - 352
    _mask = _data(844, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = '@|bK=NS-nB9Kn}AHfaw<d<`7CXypXO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
