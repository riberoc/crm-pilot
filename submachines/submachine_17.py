import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 402) - 766
    _mask = _data(669, None)
    _enc = 0
    return _mask, _enc

def run():
    matrix = '~{?M`!gd_c/ZT]@#V ^M6q~JwJmztg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
