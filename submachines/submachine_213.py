import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 399) - 349
    _mask = _data(955, None)
    _enc = 215
    return _mask, _enc

def run():
    matrix = ' ;MbOvCd~1kLyyQNS}r:ke+?`MoM;]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
