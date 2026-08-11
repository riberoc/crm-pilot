import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 133) - 141
    _mask = _data(441, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'U62gSL5H@DODAWHH.*G:%w1F=]8 8+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
