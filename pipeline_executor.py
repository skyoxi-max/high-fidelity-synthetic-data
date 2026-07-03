import numpy as np


class DatasetSimulationEngine:
    """
    Simulates multi-spectral video matrix feeds mimicking UA-DETRAC, DAWN,
    and ExDark profiles under severe degradation and low illumination.
    """

    def __init__(self, baseline_samples=100):
        self.samples = baseline_samples

    def generate_synthetic_stream(self, extreme_low_lux=True):
        """
        Creates a sequential matrix representing low-lux (Lux < 10) frames.
        """
        stream = []
        for _ in range(self.samples):
            if extreme_low_lux:
                # Heavily underexposed frame matrix simulation (Pixel values capped low)
                frame = np.random.randint(2, 28, size=(64, 64, 3), dtype=np.uint8)
            else:
                frame = np.random.randint(100, 200, size=(64, 64, 3), dtype=np.uint8)
            stream.append(frame)
        return stream

    def compute_sensor_snr(self, original_matrix, cleaned_matrix):
        """
        Calculates the actual Signal-to-Noise Ratio (SNR) improvement step.
        """
        signal_power = np.mean(cleaned_matrix.astype(np.float64) ** 2)
        noise_matrix = original_matrix.astype(np.float64) - cleaned_matrix.astype(np.float64)
        noise_power = np.mean(noise_matrix ** 2) + 1e-7

        snr_db = 10 * np.log10(signal_power / noise_power)
        return abs(snr_db)