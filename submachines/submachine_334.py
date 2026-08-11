import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 711) - 763
    _mask = _data(310, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = '(S eWs8Um%?`BVZFz]%R7IeG`#@Hog'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
