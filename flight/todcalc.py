#! Python3
"""Simple script to calculate top of descent. For flight simulation only. Not to be used for real life navigation."""
import click
import logging


def calculate_descent_rate(target, start,  descent_rate):
    """Calculate descent rate from required altitude."""
    difference = start - target
    time = int(difference / descent_rate)
    distance = (difference * 3) / 1000
    return_data = {"time": time, "distance": distance}
    return return_data


@click.command()
@click.option('--target', '-t', prompt='Target Altitude:', help='Target Altitude.', required=True, type=int)
@click.option('--start', '-s',  prompt='Starting Altitude: ', help='Starting Altitude.', required=True, type=int)
@click.option('--descent_rate', '-dr', prompt='Descent Rate: ', help='Descent Rate.', required=True, type=int)
def cli(target, start,  descent_rate):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    calculation_result = calculate_descent_rate(target, start, descent_rate)
    # Print the answers!
    logging.info(" Start descent: " + str(calculation_result["time"]) + " minutes prior to target location")
    logging.info(" Start descent: " + str(calculation_result["distance"]) + " miles from target location")
