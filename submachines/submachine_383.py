import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 350) - 106
    _mask = _data(489, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'f(f!AZXRSHt^e_|&jCq #fpiDDv8io'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
