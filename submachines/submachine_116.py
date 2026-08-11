import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 268) - 947
    _mask = _data(1328, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = '-akocO7|I5 ?KupYplk{@78bmC`|dl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
