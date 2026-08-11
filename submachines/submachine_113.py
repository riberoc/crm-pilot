import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 969) - 588
    _mask = _data(440, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = '.{Ry@Xx{07~3(^ NThe3r_x>Bg1zq.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
