import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 568) - 623
    _mask = _data(271, None)
    _enc = 212
    return _mask, _enc

def run():
    matrix = '3A)]c0~KZPsJv0lBf-$TZ?kD*ETs 5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
