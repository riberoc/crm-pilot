import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 542) - 305
    _mask = _data(889, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = 'RBGM1`UrzYReFKr=_>h<_je` x5UKI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
