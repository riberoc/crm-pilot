import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 985) - 271
    _mask = _data(572, None)
    _enc = 221
    return _mask, _enc

def run():
    matrix = 'C^QZ<A|7Ai{ q56&GX14Y&#dfu@Xyz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
