import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 112) - 166
    _mask = _data(337, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '%st>gR3N3Y8J>&K *0+yg/`Ex|:ug-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
