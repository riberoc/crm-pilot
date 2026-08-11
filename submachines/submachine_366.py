import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 252) - 315
    _mask = _data(737, None)
    _enc = 251
    return _mask, _enc

def run():
    matrix = 'z$?N=>IDG9xx[^KH_2{zk}-b| ##Kz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
