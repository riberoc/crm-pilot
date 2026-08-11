import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 947) - 443
    _mask = _data(456, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = 'xYn1G}N^v|$N{8Wu<Y6DM#=DR> p)4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
