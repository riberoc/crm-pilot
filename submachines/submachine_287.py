import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 256) - 678
    _mask = _data(1005, None)
    _enc = 79
    return _mask, _enc

def run():
    matrix = '~U@nnKD; _S+lc1Q0e<h[3Ba=5jPNl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
