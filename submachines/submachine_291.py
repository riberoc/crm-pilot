import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 179) - 545
    _mask = _data(640, None)
    _enc = 20
    return _mask, _enc

def run():
    matrix = 'u4Q6fL mX|.VNa`quk^~.%t!TTg9$F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
