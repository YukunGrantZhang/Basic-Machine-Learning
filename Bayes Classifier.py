# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:39:15 2020

@author: Grant
"""

import scipy.stats

def marginal(x, prior_f, prior_m):
    return prior_f * (scipy.stats.norm(165.1, 8.89).pdf(x)) + prior_m * scipy.stats.norm(177.8, 10.16).pdf(x)

def posterior_f(x, prior_f, prior_m):
    return scipy.stats.norm(165.1, 8.89).pdf(x) * prior_f / marginal(x, prior_f, prior_m)

def posterior_m(x, prior_f, prior_m):
    return scipy.stats.norm(177.8, 10.16).pdf(x) * prior_m / marginal(x, prior_f, prior_m)

x = 175

prior_f = 0.5
prior_m = 0.5

classifier = 0 * posterior_f(x, prior_f, prior_m) + 1 * posterior_m(x, prior_f, prior_m)

if classifier >= 0.5:
    print(f"For height {x}, it is most likely M")
else:
    print(f"For height {x}, it is most likely F")