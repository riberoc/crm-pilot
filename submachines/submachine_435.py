import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 287) - 358
    _mask = _data(856, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'wwV(7v5Ehyd#HTkrO^&;8C_D !6!6Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
