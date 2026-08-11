import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 956) - 501
    _mask = _data(291, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = ' 3V#:0w0Cy#xuIAjK3l`:JLV}?8&J)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
