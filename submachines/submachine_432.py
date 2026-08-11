import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 551) - 346
    _mask = _data(112, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = '17Wx#];2l=Tflo5T@JWjSTHUaXt=1k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
