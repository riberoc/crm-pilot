import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 547) - 701
    _mask = _data(401, None)
    _enc = 236
    return _mask, _enc

def run():
    matrix = 'KE-/BGtyNX7SQWr*c~OuCKXYucPP}?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
