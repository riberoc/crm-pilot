import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 216) - 327
    _mask = _data(665, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = 'D*/?H 772.*5{|$R,2Fddi79^!1#-1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
