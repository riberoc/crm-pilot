import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 813) - 877
    _mask = _data(1855, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'U[flgURo.7nFH6)Qe5#{&*N).= }L/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
