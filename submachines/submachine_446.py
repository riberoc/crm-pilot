import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 578) - 690
    _mask = _data(165, None)
    _enc = 36
    return _mask, _enc

def run():
    matrix = 'qQ?K;O(]UF(SaL@}x ;@s;T8t.ZT)K'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
