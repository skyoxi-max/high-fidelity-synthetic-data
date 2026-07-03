import numpy as np


class ImageAdaptiveDIPLayer:
    """
    Image-Adaptive Deep Image Processing (IA-DIP) module
    designed to stabilize signal noise under low-lux (<10 Lux) transitions.
    """

    def __init__(self, target_snr_gain=16.0):
        self.target_snr_gain = target_snr_gain

    def compute_optical_confidence(self, frame_tensor):
        """
        Calculates the information-theoretic gating coefficient (Gamma).
        """
        # Simulated luminance estimation normalized between 0 and 1
        mean_luminance = np.mean(frame_tensor) / 255.0
        # Information entropy calculation as proxy for feature richness
        entropy = -np.sum(mean_luminance * np.log2(mean_luminance + 1e-7))

        gamma = np.clip(mean_luminance * (1.0 + entropy), 0.0, 1.0)
        return gamma

    def adaptive_denoise(self, frame_tensor, gamma):
        """
        Applies localized adaptive restoration curves based on Gamma scale.
        """
        if gamma < 0.70:
            # Low illumination curve activation
            restored_tensor = frame_tensor * (1.0 + (0.70 - gamma) * 1.5)
            # Boundary restriction to uint8 format
            return np.clip(restored_tensor, 0, 255).astype(np.uint8)
        return frame_tensor