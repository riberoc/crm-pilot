import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 362) - 425
    _mask = _data(864, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'JsM,NJ9OCU,/QZM^Q.a{@y?k0r@K6x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
