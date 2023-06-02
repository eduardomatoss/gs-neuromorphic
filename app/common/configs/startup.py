from logging import getLogger

from dynaconf import settings

from app.database.connection import create_session
from app.database.models import Temperature as TemperatureModel
from app.services.thingspeak_api import ThingspeakApiClient

logger = getLogger()


def load_seed():
    thingspeak_api_client = ThingspeakApiClient(uri=settings("thingspeak_api_url"))

    db = create_session()

    logger.info("Getting temperature data in thingspeak api")

    thingspeak_list = thingspeak_api_client.get_data()

    logger.info("Saving temperature data in the database")

    for thingspeak_data in thingspeak_list.feeds:
        try:
            db_temperature = TemperatureModel(
                temperature_dht=thingspeak_data.temperature_dht,
                humidity_dht=thingspeak_data.humidity_dht,
                temperature_ext=thingspeak_data.temperature_ext,
                temperature_int=thingspeak_data.temperature_int,
                temperature_bmp=thingspeak_data.temperature_bmp,
                airpreassure=thingspeak_data.airpreassure,
                ligth_infrared=thingspeak_data.ligth_infrared,
                ligth_lux=thingspeak_data.ligth_lux,
            )
            db.add(db_temperature)
            db.commit()
        except Exception as error:
            logger.error(error)

    logger.info("Saved temperature in database")
