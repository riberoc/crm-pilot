import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 943) - 686
    _mask = _data(57, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = '@ HDwBa2q2XCrTKu0c{Txay1|AVodf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
