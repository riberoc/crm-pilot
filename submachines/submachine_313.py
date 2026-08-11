import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 910) - 343
    _mask = _data(757, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = 'F1o@Ft6v#5fcz;{ >BQq4eZ<OJDF:P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
