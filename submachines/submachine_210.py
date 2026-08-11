import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 971) - 443
    _mask = _data(343, None)
    _enc = 232
    return _mask, _enc

def run():
    matrix = 'Ed7At8~mo @e>Xw$g0PIDFb80,Q^>H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
