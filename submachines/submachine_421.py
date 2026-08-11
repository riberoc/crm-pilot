import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 494) - 877
    _mask = _data(1469, None)
    _enc = 239
    return _mask, _enc

def run():
    matrix = '6Wsc!_;a{ D56@V;Q)p[Q$YKs#>6}e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
