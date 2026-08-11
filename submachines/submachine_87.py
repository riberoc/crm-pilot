import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 735) - 331
    _mask = _data(934, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'w5:>@h)QMdlhaw:>I_Q}:yp?V` jx9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
