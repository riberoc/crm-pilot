import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 303) - 579
    _mask = _data(569, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = '$ []lxeFNgPX6z$&_ykZBmZEv1AK:>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
