import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 881) - 166
    _mask = _data(523, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = '[/#nB]5g/{u~=Xa]pHT3n?%tFKO[3?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
