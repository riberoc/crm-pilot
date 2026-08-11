import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 978) - 103
    _mask = _data(749, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'A<m3H<S.3:ck6w&<[wo e[Gf10l;]c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
