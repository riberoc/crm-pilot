import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 225) - 410
    _mask = _data(628, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'N<R=#$.2M$~(`#b+@3!K.[F*I#W3 i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
