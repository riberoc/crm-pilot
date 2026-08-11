import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 414) - 437
    _mask = _data(994, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'i-@I.&9^ky%u4K&[H(88 zjR$z5ywA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
