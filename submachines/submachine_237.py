import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 877
    _mask = _data(502, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = ';HH!2]vC= L(&cTBAkk!3D@`{-GNI$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
