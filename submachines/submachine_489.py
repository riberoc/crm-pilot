import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 106) - 212
    _mask = _data(344, None)
    _enc = 76
    return _mask, _enc

def run():
    matrix = '%3l5f|U@wPH7/)@`=7dr6v*kn_f!O<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
