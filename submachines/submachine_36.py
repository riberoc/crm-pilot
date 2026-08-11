import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 717) - 460
    _mask = _data(103, None)
    _enc = 194
    return _mask, _enc

def run():
    matrix = 'C*qQhIH:?Hv1W.%qbdZGnqg^DFsA O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
