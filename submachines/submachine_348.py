import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 384
    _mask = _data(802, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = 'Z2{XAl/BRs Z7T*zF{/E~8)-^2(d*0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
