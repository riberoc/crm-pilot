import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 142) - 592
    _mask = _data(576, None)
    _enc = 124
    return _mask, _enc

def run():
    matrix = 'W3 -{PqG!Fx4zO9)BQSe|ab^z&E>,~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
