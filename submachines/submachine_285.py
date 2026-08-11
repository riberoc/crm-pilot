import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 987) - 554
    _mask = _data(267, None)
    _enc = 160
    return _mask, _enc

def run():
    matrix = '/{sH9_ `;5xz~>>R>VU}2),dxt<?Vv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
