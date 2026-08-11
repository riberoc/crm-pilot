import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 827) - 269
    _mask = _data(583, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = '6ohnS2eUMX]Msl3L)3LMS{28=.A7kZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
