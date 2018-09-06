#import bezier
import numpy as np

nodes1 = np.asfortranarray([[0.0, 0.5, 1.0],[0.0, 1.0, 0.0]])
curve1 = bezier.Curve(nodes1, degree=2)