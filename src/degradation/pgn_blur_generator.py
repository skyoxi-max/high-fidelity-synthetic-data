import cv2
import numpy as np

def apply_poisson_gaussian_noise(image: np.ndarray, alpha: float = 0.05, sigma_read: float = 25.0) -> np.ndarray:
    """
    Applies compound Poisson-Gaussian noise (PGN) modeling sensor shot and read noise.
    I_noisy = alpha * Poisson(I_clean / alpha) + Gaussian(0, sigma_read^2)
    """
    img_float = image.astype(np.float32)
    
    # Photon shot noise (Poisson)
    scaled_img = np.maximum(img_float / alpha, 0)
    poisson_noise = np.random.poisson(scaled_img) * alpha
    
    # Read noise (Gaussian)
    gaussian_noise = np.random.normal(0, sigma_read, image.shape)
    
    noisy_img = poisson_noise + gaussian_noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)

def apply_gaussian_blur(image: np.ndarray, sigma_b: float = 8.0) -> np.ndarray:
    """
    Applies extreme spatial low-pass filtering simulating lens condensation/fog.
    Kernel size derived dynamically from sigma_b.
    """
    ksize = int(6 * sigma_b + 1) | 1  # Ensure odd kernel size
    return cv2.GaussianBlur(image, (ksize, ksize), sigmaX=sigma_b, sigmaY=sigma_b)

if __name__ == "__main__":
    # Test stub for data generation
    dummy_frame = np.random.randint(0, 256, (640, 640, 3), dtype=np.uint8)
    pgn_frame = apply_poisson_gaussian_noise(dummy_frame, alpha=0.05, sigma_read=30.0)
    blurred_frame = apply_gaussian_blur(dummy_frame, sigma_b=8.0)
    print("Degradation generator verified successfully.")
