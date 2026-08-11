import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 429) - 646
    _mask = _data(712, None)
    _enc = 200
    return _mask, _enc

def run():
    matrix = '9d.)UW!v5{6V/I=Q*r6{K<4 bAbiR-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
