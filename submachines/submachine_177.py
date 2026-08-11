import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 111
    _mask = _data(454, None)
    _enc = 122
    return _mask, _enc

def run():
    matrix = 'i.Jfwj`BW=|;(WIhF4.rWMUN&?(~ r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
