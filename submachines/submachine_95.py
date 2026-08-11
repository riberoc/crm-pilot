import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 382) - 313
    _mask = _data(882, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = 'yscqky92!F; PkLCMz.uN+v5|/&ESp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
