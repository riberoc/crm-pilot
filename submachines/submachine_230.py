import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 356) - 443
    _mask = _data(868, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = '2iz<$ (Hyi}Y5-XOO:R.Y^QHH^`$kW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
