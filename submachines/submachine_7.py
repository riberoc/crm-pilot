import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 657) - 143
    _mask = _data(577, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = '.2Bn%2asE7s.98x=T5g~aZ`|;3?,2>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
