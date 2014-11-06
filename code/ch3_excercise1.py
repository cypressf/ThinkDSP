from thinkdsp import *
import thinkplot


class SawtoothChirp(Chirp):

    def _evaluate(self, ts, freqs):
        """Helper function that evaluates the signal.

        ts: float array of times
        freqs: float array of frequencies during each interval
        """
        dts = numpy.diff(ts)
        # dps = PI2 * freqs * dts
        dcycles = freqs * dts
        cycles = numpy.cumsum(dcycles)
        cycles = numpy.insert(cycles, 0, 0)
        frac, _ = numpy.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

if __name__ == "__main__":
    sawtooth = SawtoothSignal()
    sawtooth_wave = sawtooth.make_wave()
    chirp = SawtoothChirp()
    wave = chirp.make_wave(duration=1, framerate=10000)
    segment = wave.segment(duration=0.02)
    segment.plot()
    wave.play()
    thinkplot.show()