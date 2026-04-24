"""Utility functions for common operations."""

from typing import Any, List


def validate_string(value: str, min_length: int = 1) -> bool:
    """Validate string input.
    
    Args:
        value: String to validate
        min_length: Minimum required length
        
    Returns:
        True if valid, False otherwise
    """
    return isinstance(value, str) and len(value) >= min_length


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list.
    
    Args:
        nested_list: List that may contain nested lists
        
    Returns:
        Flattened list
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks.
    
    Args:
        items: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
