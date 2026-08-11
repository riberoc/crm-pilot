import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 297) - 442
    _mask = _data(220, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = 'J1x=Jt`vU?Mv%2@@[FmH!pHX<wN! f'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
