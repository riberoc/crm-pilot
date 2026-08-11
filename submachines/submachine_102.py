import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 464) - 261
    _mask = _data(116, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = 'o?Ud|dBY%DEQVjc/j,<@WMK:>zT_O.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
