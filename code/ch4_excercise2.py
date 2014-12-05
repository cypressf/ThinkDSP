from thinkdsp import *
import thinkplot

if __name__ == "__main__":
    cymbal = read_wave("75341__neotone__cymbol-scraped.wav")
    cymbal_spectrum = cymbal.make_spectrum()
    cymbal_spectrum.low_pass(15000)
    cymbal_spectrum.plot()
    cymbal_filtered = cymbal_spectrum.make_wave()
    # cymbal_filtered.play()
    thinkplot.config(yscale="log", xscale="log")
    pyplot.show()

    # cymbal.play()
