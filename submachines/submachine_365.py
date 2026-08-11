import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 771) - 265
    _mask = _data(693, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = ';Br/.CV K>WmPNzd#{d2UtpgD.4o@R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
