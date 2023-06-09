import logging
import aiohttp

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity, ENTITY_ID_FORMAT
import homeassistant.helpers.config_validation as cv


CONF_MARKET_CODE = "market_code"


_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass,config,async_add_entities,discovery_info=None):
    market_code = config[CONF_MARKET_CODE]

class ReweOfferSensor():
    def __init__(self, market_code):
        self._market_code = market_code

    @Property
    def market_code(self):
        return self._market_code
   
    async def get_data(self):
        """ fetch data from the REWE API """
        base_url = f"https://mobile-api.rewe.de/api/v3/all-offers?marketCode={self._market_code}"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(base_url) as resp:
                    offers = await resp.json()
            except:
                _LOGGER.error(f"Failed to get offers from API")
                return