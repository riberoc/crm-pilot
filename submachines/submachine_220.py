import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 111) - 113
    _mask = _data(319, None)
    _enc = 204
    return _mask, _enc

def run():
    matrix = 'hV4Rxhb=/zQ0kl;*Ue[ V]k$iN?}r_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
