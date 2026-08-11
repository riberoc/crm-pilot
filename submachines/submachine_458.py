import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 830) - 577
    _mask = _data(341, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'UTnpsWpS=zt(9avD|^DKTq0)igQ4Je'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
