import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 282) - 982
    _mask = _data(1347, None)
    _enc = 149
    return _mask, _enc

def run():
    matrix = ',R~kV,jN=:]!.>W4FLu^b. -aC%=Ed'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
