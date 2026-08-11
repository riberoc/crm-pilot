import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 511) - 936
    _mask = _data(1413, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = 'NrMGe89B>Wtxrk ?Fc<]0hlL6^PJYt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
