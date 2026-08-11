import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 967) - 747
    _mask = _data(76, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = '/YXV.h0a=sLHt:B0EPE/O2&2h>(PS*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
