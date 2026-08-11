import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 547) - 659
    _mask = _data(328, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = '6j+em3Vxg)H CR70!F~U;u~44I~xSc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
