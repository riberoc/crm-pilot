import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 396) - 268
    _mask = _data(199, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = '[tJ;KEk:2Xe(XGT/5z<O$Bpnm~LCj '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
