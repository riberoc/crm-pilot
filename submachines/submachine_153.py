import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 685) - 477
    _mask = _data(863, None)
    _enc = 0
    return _mask, _enc

def run():
    matrix = '_4{=v0Rk^HmWSf>bp[&EX ~0(^.pNx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
