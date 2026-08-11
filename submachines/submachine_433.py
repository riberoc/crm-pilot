import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 707) - 742
    _mask = _data(434, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = '~qxu9P^ GI6oT/`:.[CNOx4)28[,bL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
