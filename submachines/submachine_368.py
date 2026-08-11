import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 481) - 523
    _mask = _data(876, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = 'YmQ*vXdruzom[M<f$cdpwGG<I!}a H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
