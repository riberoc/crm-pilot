import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 528) - 613
    _mask = _data(282, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'VyK*(dYEw>EVVls7v1Dh J5hX.AEb@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
