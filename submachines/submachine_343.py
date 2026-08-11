import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 604) - 967
    _mask = _data(1558, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = ']@QOoQic(Q5z7*d ?Et:CGul/8e:iR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
