import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 978) - 340
    _mask = _data(685, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = '#{]=8j #U`.~2Eui$Gw,=TYk}3OKsp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
