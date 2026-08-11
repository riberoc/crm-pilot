import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 858) - 413
    _mask = _data(274, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '_8y-&Ud,>QrNtb?P.iL$E^aGv.4@:p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
