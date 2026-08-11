import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 871) - 599
    _mask = _data(282, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = 'p{0l-9tbMb*rrF@^tc-F)C36/JdBo4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
