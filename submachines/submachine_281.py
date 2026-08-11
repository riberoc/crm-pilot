import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 747) - 656
    _mask = _data(430, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'QAW1*25F3dH22fS w.fcVbtn0tS?Y%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
