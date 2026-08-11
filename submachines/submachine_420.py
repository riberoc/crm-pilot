import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 338) - 204
    _mask = _data(69, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = '(Axm#:<-VMA^i833)Zzp0#FV<Nx FL'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
