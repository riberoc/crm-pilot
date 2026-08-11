import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 518) - 474
    _mask = _data(77, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '7<0Du 1d#5j&QU!%}!LSi`/@D?E#O9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
