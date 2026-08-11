import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 528) - 725
    _mask = _data(317, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'gQ}e(XjB3WPZCq{A>x%#^0ENFxGP 2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
