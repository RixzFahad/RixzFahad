"""Core module with main functionality."""

from typing import Any, Dict, List


class DataProcessor:
    """Process and transform data."""

    def __init__(self):
        """Initialize the DataProcessor."""
        self.data: List[Dict[str, Any]] = []

    def add_item(self, item: Dict[str, Any]) -> None:
        """Add an item to the data list.
        
        Args:
            item: Dictionary item to add
        """
        self.data.append(item)

    def get_items(self) -> List[Dict[str, Any]]:
        """Retrieve all stored items.
        
        Returns:
            List of all stored items
        """
        return self.data

    def clear(self) -> None:
        """Clear all stored items."""
        self.data = []

    def count(self) -> int:
        """Get the count of stored items.
        
        Returns:
            Number of items
        """
        return len(self.data)
