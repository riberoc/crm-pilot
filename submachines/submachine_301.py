import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 335) - 599
    _mask = _data(984, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = 'mv%*yM7y_NT-A DCZ1D)%1y|As4]A*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
