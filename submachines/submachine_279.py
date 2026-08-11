import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 555) - 796
    _mask = _data(486, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = ' <Ss@Umx#+HGRKS5*uEe93VY<1p2R>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
