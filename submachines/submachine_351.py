import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 701) - 476
    _mask = _data(5, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'h9Ty?/B0#<&eVnm}FlSB^i[rHxky^a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
