import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 862) - 555
    _mask = _data(430, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = 'Gv*C$>xBjKMM@Gg5U6^<zyY^8 NfzJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
