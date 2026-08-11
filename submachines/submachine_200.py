import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 958
    _mask = _data(453, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = 'Vmp5nZF5Wju Xf,2vy1@>[ELR(=C1q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
