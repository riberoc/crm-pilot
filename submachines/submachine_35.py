import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 393) - 705
    _mask = _data(515, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = '0>qo%}vgzy8{f7E3<M1yoW,y4t^P/6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
