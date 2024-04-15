import numpy as np

def generate_gaussian_noise(self,epsilon, delta):
    sigma = np.sqrt(2 * np.log(1.25 / self.delta)) * (1/ self.epsilon)
    noise = np.random.normal(0, sigma)
    return noise