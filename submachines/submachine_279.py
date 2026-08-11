import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 951) - 832
    _mask = _data(96, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = '-jW0o,.gd`V[3cZm^^`<nN Cd~Q(w+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
