import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 129) - 833
    _mask = _data(979, None)
    _enc = 26
    return _mask, _enc

def run():
    matrix = ']5nSj11Q^q7 QC#,[t5}POUjBL#z;H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
