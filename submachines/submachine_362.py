import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 196) - 814
    _mask = _data(851, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = '>5<8`!^00M?FvP #9/Kjzpr2CE@9.f'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
