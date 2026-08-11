import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 672) - 744
    _mask = _data(501, None)
    _enc = 124
    return _mask, _enc

def run():
    matrix = 'AKT^N61Igy.M]Z`*p bJj5f((#!)]&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
