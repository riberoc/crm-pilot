import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 987) - 341
    _mask = _data(599, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = '/|Qeoi G%4D~qA0_GF07Dy.BT4FB(S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
