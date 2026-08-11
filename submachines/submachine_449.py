import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 516) - 331
    _mask = _data(867, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = 'x:su!+_( 1Lv-{^!}bj?[HY}LNP?&T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
