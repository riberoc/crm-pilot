import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 573) - 782
    _mask = _data(398, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = '#h/bCGuljy-1yOf9mJ1ys.3!W#)+8}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
