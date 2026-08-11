import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 117) - 616
    _mask = _data(716, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = 'O<lfeKy!Hu;S =at{-OTiRX.!G>e5B'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
