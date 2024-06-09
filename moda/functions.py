import re
import json

from moda.logger import get_logger

logger = get_logger()


def get_functions_metadata(functions) -> list:
    functions_metadata = []
    for function in functions:
        functions_metadata.append({
            "type": "function",
            "function": {
                "name": function["name"],
                "description": function["description"] + function["condition"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Text of question which user asked"
                        }
                    },
                    "required": [
                        "question"
                    ]
                }
            }
        })
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
