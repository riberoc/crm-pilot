import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 502
    _mask = _data(92, None)
    _enc = 33
    return _mask, _enc

def run():
    matrix = 'A4~V<ln OY>JRg0|LgQzpg}Y,ae/34'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
