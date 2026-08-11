import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 726) - 934
    _mask = _data(1763, None)
    _enc = 150
    return _mask, _enc

def run():
    matrix = '$cC/A=6En_mUx:2s($J+,2);` 5Y8*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
