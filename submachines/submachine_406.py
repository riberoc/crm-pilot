import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 296) - 917
    _mask = _data(1364, None)
    _enc = 235
    return _mask, _enc

def run():
    matrix = 'm=~r(<C~b[.2 S.2:(xM$v_JMPt~F{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
