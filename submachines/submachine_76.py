import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 269) - 943
    _mask = _data(1394, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = '(7x|~ca7O(^>13EQeW1z_D .7&4A$|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
