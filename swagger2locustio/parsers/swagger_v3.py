"""Module: SwaggerV3 parser"""

from swagger2locustio.parsers.base_parser import SwaggerBaseParser


class SwaggerV3Parser(SwaggerBaseParser):
    """Class: SwaggerV3 parser"""

    @staticmethod
    def _parse_params(params: dict) -> dict:
        param_data = {}
        for param in params:
            param_name = param.get("name")
            # if not param_name or not param.get("default") or not param.get("in"):
            if not param_name or not param.get("in"):
                if param.get("required"):
                    raise ValueError("Not full info about required param")
                continue
            param_data[param_name] = deepcopy(param)
        return param_data
