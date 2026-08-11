import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 338
    _mask = _data(809, None)
    _enc = 243
    return _mask, _enc

def run():
    matrix = 'FlY<(>H2TnGG5Eb@JV9.Krx&T:5t}H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
