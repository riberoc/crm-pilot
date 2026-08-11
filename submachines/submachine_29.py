import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 612) - 254
    _mask = _data(1021, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = '5UJ|9U<!CT%fM#&z:9#y7 >smesh^A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
