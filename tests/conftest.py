"""
This is a general logging fixture for all type of tests
"""

import pytest
import logging


# Logging Setup
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@pytest.fixture(scope="session")
def logger():
    """
    This is a logger for all tests
    scope="session" - means that it is created once for complete testing session
    """
    return logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def test_run_setup(logger):
    """
    This fixture is used for each test
    autouse=True - means that it is launching automatically
    """
    logger.info("=" * 80)
    logger.info("Start of test")
    logger.info("=" * 80)
    yield
    logger.info("=" * 80)
    logger.info("End of test")
    logger.info("=" * 80)
