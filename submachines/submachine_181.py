import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 216) - 897
    _mask = _data(791, None)
    _enc = 74
    return _mask, _enc

def run():
    matrix = 'oDd/ >:f9$CkR2h+>Z*&#1d0ibFDne'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
