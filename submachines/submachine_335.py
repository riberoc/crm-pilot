import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 738) - 971
    _mask = _data(1626, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = '9W4u*ubQ$yxbe7%y1<N ;{i3AT>4S-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
