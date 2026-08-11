import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 141) - 914
    _mask = _data(825, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = 'C^-C7 un/zQ56-]Ik<SwXjN};Hsad5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
