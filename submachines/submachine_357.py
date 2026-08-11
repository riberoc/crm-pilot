import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 110) - 307
    _mask = _data(268, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'cU!v^6xGncN|0/*vK6x[`_kqrf*B(('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
