import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 235) - 841
    _mask = _data(803, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = '!#R1G;R{cw.kZ##$0U^{NU7lztR;x/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
