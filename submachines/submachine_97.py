import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 258) - 528
    _mask = _data(1015, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = '2b8f]VVnSPh6bOsf%QQ4Wn;cAYg~cq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
