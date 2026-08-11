import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 832) - 268
    _mask = _data(611, None)
    _enc = 27
    return _mask, _enc

def run():
    matrix = '0XiGE^D/.i`6 R2g^WT^+d;tEa{eDF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
