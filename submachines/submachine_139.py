import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 928) - 886
    _mask = _data(1942, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 's#90<8 n!#YoI:[Gm)cJ9PVU3i<vF2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
