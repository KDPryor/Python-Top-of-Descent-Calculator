#! Python3
"""Simple script to calculate your top of descent."""
import click
import logging


def calculate_decent_rate(target, start,  decent_rate):
    """Calculate decent rate from required altitude."""
    difference = start - target
    time = int(difference / decent_rate)
    distance = (difference * 3) / 1000
    return_data = {"time": time, "distance": distance}
    return return_data


@click.command()
@click.option('--target', '-t', prompt='Target Altitude:', help='Target Altitude.', required=True, type=int)
@click.option('--start', '-s',  prompt='Starting Altitude: ', help='Starting Altitude.', required=True, type=int)
@click.option('--decent_rate', '-dr', prompt='Decent Rate: ', help='Descent Rate.', required=True, type=int)
def cli(target, start,  decent_rate):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    calculation_result = calculate_decent_rate(target, start, decent_rate)
    # Print the answers!
    logging.info(" Start descent: " + str(calculation_result["time"]) + " minutes prior to target location")
    logging.info(" Start descent: " + str(calculation_result["distance"]) + " miles from target location")
