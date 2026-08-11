import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 692) - 148
    _mask = _data(998, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'Q8}5u4B{JsoH%1[%@z3;2!FIa&%lS#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
