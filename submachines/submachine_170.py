import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 282) - 850
    _mask = _data(1332, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = '!aMonI23wW?R,~<W;OAd*y` B0Ho10'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
