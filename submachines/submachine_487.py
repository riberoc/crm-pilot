import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 211) - 569
    _mask = _data(593, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'ni-X=i)1 ]Dc@b+;kAqhaM--<^D%D;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
