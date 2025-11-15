import logging

logging.basicConfig(level=logging.INFO, filename="year.log", filemode="w", format="Year-Month-Day :  %(message)s")
logging.info("2025:11:Saturday")
