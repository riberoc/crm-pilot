import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 859) - 879
    _mask = _data(245, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'Q)<((h2uw6l 93!Nb!)@PN]k)5jo<u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
