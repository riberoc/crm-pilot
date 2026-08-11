import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 197) - 290
    _mask = _data(294, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'D[Pn=,1;+:B`S+|H(x QlB{vwb`~<~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
