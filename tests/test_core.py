"""Tests for core module."""

import pytest
from src.core import DataProcessor


class TestDataProcessor:
    """Test cases for DataProcessor class."""

    @pytest.fixture
    def processor(self):
        """Create a DataProcessor instance."""
        return DataProcessor()

    def test_initialization(self, processor):
        """Test DataProcessor initialization."""
        assert processor.data == []
        assert processor.count() == 0

    def test_add_item(self, processor):
        """Test adding items to processor."""
        item = {"name": "test", "value": 42}
        processor.add_item(item)
        assert processor.count() == 1
        assert processor.get_items()[0] == item

    def test_add_multiple_items(self, processor):
        """Test adding multiple items."""
        items = [{"id": i} for i in range(5)]
        for item in items:
            processor.add_item(item)
        assert processor.count() == 5

    def test_clear(self, processor):
        """Test clearing the processor."""
        processor.add_item({"test": "data"})
        assert processor.count() == 1
        processor.clear()
        assert processor.count() == 0
        assert processor.get_items() == []
