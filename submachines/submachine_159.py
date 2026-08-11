import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 450) - 189
    _mask = _data(144, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = 'glthn1_*6*d 3lg|va~ny2K~o,DJ}y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
