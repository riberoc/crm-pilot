import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 440) - 683
    _mask = _data(834, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'PVA#&^:h[-aT# MlpoU3i@-aE<yK(Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
