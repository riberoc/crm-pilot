import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 299) - 503
    _mask = _data(951, None)
    _enc = 171
    return _mask, _enc

def run():
    matrix = 'i|IzNEb99Yy3`9i@P<-{PhlM<psJ1;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
