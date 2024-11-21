import soundfile as sf
import pyloudnorm as pyln
import numpy as np


def linear_to_db(linear: float) -> float:
    return 20 * np.log10(linear) if linear > 0.0000000001 else -200

def get_peak_amplitude(audio_path):
    data, rate = sf.read(audio_path)
    peak = np.max(data)

    return linear_to_db(peak)


def normalize_audio_file(audiopath, target_audio_path, target_loudness=-12.0):
    data, rate = sf.read(audiopath)

    peak_normalized_audio = pyln.normalize.peak(data, target_loudness)
    # print(sf.info(audiopath, True))
    sf.write(target_audio_path, peak_normalized_audio, rate)


