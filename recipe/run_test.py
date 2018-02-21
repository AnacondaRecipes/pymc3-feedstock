import os
# theano >= 1.0.0
os.environ['MKL_THREADING_LAYER']='GNU'

import pymc3
import pymc3.backends
import pymc3.distributions
import pymc3.examples
import pymc3.external
import pymc3.glm
import pymc3.gp
import pymc3.plots
import pymc3.step_methods
import pymc3.step_methods.hmc
import pymc3.tests
import pymc3.tuning
import pymc3.variational
