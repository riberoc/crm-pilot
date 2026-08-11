import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 575) - 440
    _mask = _data(989, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = 'E`mc1w T.,w5j~A5w-V4TVKq8QEoPH'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
