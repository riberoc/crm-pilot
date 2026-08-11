import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 867) - 313
    _mask = _data(355, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'vRZ_SiN$<14D2!kti I@Sr6/gywFwC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
