import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 477) - 214
    _mask = _data(181, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = '}o |:j$^tf(Ugj=r!,42{}{~2=([kb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
