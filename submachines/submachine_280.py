import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 639) - 622
    _mask = _data(151, None)
    _enc = 113
    return _mask, _enc

def run():
    matrix = '%b/lq(^v]T] tu;*#S4}rCI=>]w0Va'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
