import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 994) - 572
    _mask = _data(204, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = 'FLWE[<;6=*{|( ^^8{0LT7l)uZy,tA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
