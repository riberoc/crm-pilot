import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 370) - 603
    _mask = _data(1004, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'DL1X0&7F-?Vl/K9@MMEA&Wy yZU`pP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
