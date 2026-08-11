import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 837) - 541
    _mask = _data(371, None)
    _enc = 12
    return _mask, _enc

def run():
    matrix = ']~!W~eO,51eM)kN.]b&al ;)mW]r6I'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
