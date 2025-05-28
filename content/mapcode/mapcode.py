"""
mapcode.py

This module provides a framework for computing the fixed point of a function F: X -> X,
starting from an initial value x, and then mapping the result to another space using a function pi.
It includes utilities for tracing the iteration process and composing the computation as a pipeline.

Functions:
    loop(F, x): Iterates F starting from x until a fixed point is reached.
    limit_map(F): Returns a function that computes the fixed point of F starting from any x.
    mapcode(rho, F, pi): Composes rho, limit_map(F), and pi to map inputs to outputs via fixed points.

Logging:
    Uses the standard logging module to trace computation steps.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def loop(F, x):
    """
    Iterates the function F starting from x until a fixed point is reached (i.e., F(x) == x).

    Args:
        F (callable): A function from X to X.
        x: Initial value in X.

    Returns:
        The fixed point of F starting from x.
    """
    while x != F(x):
        logger.info(f"x = {x}")
        x = F(x)
    logger.info(f"x = {x}\n")
    return x

def limit_map(F):
    """
    Returns a function that computes the fixed point of F starting from any given x.

    Args:
        F (callable): A function from X to X.

    Returns:
        F_infty (callable): A function that takes x and returns the fixed point of F starting from x.
    """
    def F_infty(x):
        return loop(F, x)
    return F_infty

def mapcode(rho, F, pi):
    """
    Composes the functions rho, limit_map(F), and pi to map inputs to outputs via fixed points.

    Args:
        rho (callable): A function from I to X (initial state generator).
        F (callable): A function from X to X (state transition).
        pi (callable): A function from X to A (output extractor).

    Returns:
        f (callable): A function from I to A, computing the output for each input via fixed point iteration.
    """
    F_infty = limit_map(F)
    def f(i):
        logger.info("==========")
        logger.info(f"inst = {i}\n")
        x0 = rho(i)
        logger.info(f"init_state = {x0}\n")
        fix = F_infty(x0)
        ans = pi(fix)
        logger.info(f"ans = {ans}")
        logger.info("==========\n\n")
        return ans
    return f
