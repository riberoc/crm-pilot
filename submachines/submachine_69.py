import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 599) - 692
    _mask = _data(173, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = '0:[#tXsbxqN_8]d1]ni=a ^nc{DJ*E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
