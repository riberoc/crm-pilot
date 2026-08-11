import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 289) - 945
    _mask = _data(1280, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = '*(CVudI b1R{E-d>JjnX7s~-BW}p40'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
