import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 693) - 234
    _mask = _data(868, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = '5$Iy]q[^bG[| /htk5Ao4E;sX5$?3i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
