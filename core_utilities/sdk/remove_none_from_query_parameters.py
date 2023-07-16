from typing import Any, Dict, Optional


def remove_none_from_query_parameters(query_parameters: Dict[str, Optional[Any]]) -> Dict[str, Any]:
    new_query_params: Dict[str, str] = {}
    for query_param_key, query_param_value in query_parameters.items():
        if query_param_value is not None:
            new_query_params[query_param_key] = query_param_value
    return new_query_params
