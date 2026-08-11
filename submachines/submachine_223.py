import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 242) - 918
    _mask = _data(779, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = 'PY_e1?ZU*U[7G.fk:NxaP~{$BXzba&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
