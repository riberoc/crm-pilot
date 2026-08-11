import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 306) - 724
    _mask = _data(756, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = 't~5E7A ~Yf{U){B]_=_zY$`e|T>FZ)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
