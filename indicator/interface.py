from .plot import Scheduler


class Interface:

    def open_csv(self, file: str, start_time=None, end_time=None):
        return Scheduler.open_csv(file, start_time, end_time)

    def open_json(self, file: str, start_time=None, end_time=None):
        return Scheduler.open_json(file, start_time, end_time)

    def add_bar(self, data, opens=True):
        Scheduler.update_bar(data, opens)

    def sma(self, n=15):
        data = Scheduler.ret_close
        return Scheduler.sma(data, n)

    def ema(self, n=12, alpha=None):
        data = Scheduler.ret_close
        return Scheduler.ema(data, n, alpha)

    def wma(self, n=30):
        data = Scheduler.ret_close
        return Scheduler.wma(data, n)

    def kd(self, n=14, f=3):
        data = Scheduler.ret_close
        return Scheduler.kd(data, n, f)

    def macd(self, n=12, m=20, f=9):
        data = Scheduler.ret_close
        return Scheduler.macd(data, n, m, f)

    def rsi(self, n=14, l=1):
        data = Scheduler.ret_close
        return Scheduler.rsi(data, n, l)

    def smma(self, n=10, alpha=15):
        data = Scheduler.ret_close
        return Scheduler.smma(data, n, alpha)

    def atr(self, n=14):
        data = Scheduler.ret_close
        return Scheduler.atr(data, n)

    def stdDev(self, n=20):
        data = Scheduler.ret_close
        return Scheduler.stdDev(data, n)

    def boll(self, n=20, m=2):
        data = Scheduler.ret_close
        return Scheduler.boll(data, n, m)

    def trix(self, n=15, m=1):
        data = Scheduler.ret_close
        return Scheduler.trix(data, n, m)

    def roc(self, n=12):
        data = Scheduler.ret_close
        return Scheduler.roc(data, n)

    def mtm(self, n=12):
        data = Scheduler.ret_close
        return Scheduler.mtm(data, n)

    def tema(self, n=12):
        data = Scheduler.ret_close
        return Scheduler.tema(data, n)

    def wr(self, n=14):
        data = Scheduler.ret_close
        return Scheduler.wr(data, n)

    def UltimateOscillator(self):
        pass

    def AroonIndicator(self):
        pass

    def plot(self, width=8, height=6, color="k", lw=0.5):
        Scheduler.plot(width=width, height=height, color=color, lw=lw)


api = Interface()