# API Documentation

## Overview

This document describes the public API for the RixzFahad project.

## Core Module

### DataProcessor

Main class for processing and transforming data.

#### Methods

- `add_item(item: Dict[str, Any]) -> None` - Add an item to the data list
- `get_items() -> List[Dict[str, Any]]` - Retrieve all stored items
- `clear() -> None` - Clear all stored items
- `count() -> int` - Get the count of stored items

#### Example

```python
from src.core import DataProcessor

processor = DataProcessor()
processor.add_item({"name": "example", "value": 42})
items = processor.get_items()
print(processor.count())
```

## Utilities Module

### Functions

- `validate_string(value: str, min_length: int = 1) -> bool` - Validate string input
- `flatten_list(nested_list: List[Any]) -> List[Any]` - Flatten a nested list
- `chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]` - Split a list into chunks

## Configuration

Use the `Config` class to manage application settings:

```python
from src.config import get_config

config = get_config()
print(config.APP_NAME)
print(config.DEBUG)
```
