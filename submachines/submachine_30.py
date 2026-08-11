import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 544) - 650
    _mask = _data(333, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = 'Fh/tk,D<yiMg`O8s)=gi&jjvMxi+^ '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
