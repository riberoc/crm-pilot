import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 645) - 392
    _mask = _data(867, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = '^IyC_IXUd#?tOTB7{hga}`gJT+j:lj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
