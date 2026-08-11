import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 586) - 203
    _mask = _data(997, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = '?gG.sW;lkd[oN(XV`W$IdT~(Ob]*Hk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
