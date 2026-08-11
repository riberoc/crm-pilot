import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 160) - 975
    _mask = _data(1189, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = '{[qg]eXC}-i`=<B^s60o?p;,Z66 MD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
