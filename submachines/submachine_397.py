import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 580) - 620
    _mask = _data(292, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'V|MEvG0[(pryh[s$z0?nZ=V2SAE8|P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
