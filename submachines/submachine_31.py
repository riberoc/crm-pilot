import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 572) - 103
    _mask = _data(874, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = '#eE3V7dPW+f{quuDV-o1}=gXFoEiV '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
