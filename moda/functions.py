import re
import json

from moda.logger import get_logger

logger = get_logger()


def get_functions_metadata(functions) -> list:
    functions_metadata = []
    for function in functions:
        function_metadata = {
            "type": "function",
            "function": {
                "name": function["name"],
                "description": function["description"] + "\n" + function["condition"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of function call"
                        }
                    },
                    "required": [
                        "name"
                    ]
                }
            }
        }

        if 'examples' in function:
            function_metadata["function"]["examples"] = function["examples"]

        if 'keywords' in function:
            function_metadata["function"]["keywords"] = ', '.join(function["keywords"])

        functions_metadata.append(function_metadata)
    return functions_metadata


def extract_function_call_from_string(s) -> str | bool:
    pattern = re.compile(r'<functioncall>(.*?)</functioncall>', re.DOTALL)
    match = pattern.search(s)
    if match:
        json_str = match.group(1).strip()
        try:
            function_call = json.loads(json_str)
            return function_call
        except json.JSONDecodeError:
            logger.error("Invalid JSON format")
            return False
    else:
        logger.error("Invalid JSON format")
        return False


def has_function_call(s) -> bool:
    """Checks if string has function call"""
    return '<functioncall>' in s and '</functioncall>' in s
