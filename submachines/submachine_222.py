import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 277) - 353
    _mask = _data(771, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'c:/idn^3cY+F94>7 +3w/:I2;ZfRdk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
