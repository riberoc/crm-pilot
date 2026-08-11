import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 531) - 693
    _mask = _data(368, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = '6g`>Mem6$SoWA4XJ|Y_}XunBJm^je '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
