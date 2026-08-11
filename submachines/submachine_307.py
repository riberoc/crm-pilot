import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 713) - 332
    _mask = _data(252, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'DQU{[xnr3h:/[iNO ;7kEs~l^H_bPC'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
