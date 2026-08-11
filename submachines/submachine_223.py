import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 365) - 147
    _mask = _data(106, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'wQ0#b4M<=u)<6&y%R/#+ye?<FqeDTt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
