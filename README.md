# pytorch-lgssm
A minimal Linear Gaussian State Space Model for pytorch.

Supports sampling and can compute log(p(x)) for a batch of observed sequences x using the Kalman filtering algorithm

### Usage

```python
from lgssm import LinearGaussianStateSpaceModel

model = LinearGaussianStateSpaceModel(prior_mean, prior_covariance, transition_matrix, transition_covariance, observation_matrix, observation_covariance)
x, z = model.sample(8) #(8, x_dim), (8, z_dim)

logpx, steps = model.log_prob(x.unsqueeze(1)) # Computes log(p(x)) for a batch of sequences x
# steps contain the prior and posterior filtering distributions for x and z at each time step
```

### Installation

`pip install git+https://github.com/rasmusbergpalm/pytorch-lgssm`
