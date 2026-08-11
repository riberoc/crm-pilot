import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 392) - 163
    _mask = _data(10, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = 'Y9&roD=vzx8U+ ~$_Y5H.VH01A(~!#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
