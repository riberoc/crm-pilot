import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 270) - 539
    _mask = _data(521, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'I19p/4#G2gWUL@|+u|(n[ T1Wm!=R1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
