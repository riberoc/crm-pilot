import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 739) - 521
    _mask = _data(14, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = '=sep<DA74Rn:5QLtYnCAu#_GY@M#k4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
