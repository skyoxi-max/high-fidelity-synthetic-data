import numpy as np

class InformationTheoreticGate:
    def __init__(self, gamma_threshold: float = 0.70, alpha_th: float = 0.85):
        self.gamma = gamma_threshold
        self.alpha_th = alpha_th

    def evaluate_gate(self, visual_confidence: float) -> str:
        """
        Determines execution mode based on visual parsing confidence.
        """
        if visual_confidence < self.gamma:
            return "WIRELESS_RF_FALLBACK"
        return "PRIMARY_VISUAL_TRACKING"

    def compute_proximity_match(self, v_track: np.ndarray, drssi_dt: float, b_box_center: np.ndarray, node_coords: np.ndarray, l1: float = 0.5, l2: float = 0.5) -> float:
        """
        Calculates PMatch metric using RSSI gradient and kinematic directional vectors (Equation 9).
        """
        dist_vec = b_box_center - node_coords
        dist_norm = dist_vec / (np.linalg.norm(dist_vec) ** 2 + 1e-6)
        z = l1 * drssi_dt + l2 * np.dot(v_track, dist_norm)
        return 1.0 / (1.0 + np.exp(-z))

if __name__ == "__main__":
    gate = InformationTheoreticGate()
    print("Gate Status (Conf = 0.85):", gate.evaluate_gate(0.85))
    print("Gate Status (Conf = 0.30):", gate.evaluate_gate(0.30))
