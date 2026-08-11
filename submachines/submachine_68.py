import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 645) - 158
    _mask = _data(782, None)
    _enc = 245
    return _mask, _enc

def run():
    matrix = 'fZ!:yu2r4J0v9r25mn!`qjPP D8[F{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
