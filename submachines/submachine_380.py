import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 382) - 525
    _mask = _data(905, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = "/2=LZU'!y-|yT*v|C^yH2Cz(gD5D*x"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
