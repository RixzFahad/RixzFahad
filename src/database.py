"""Database module for data persistence."""

import json
from typing import Any, Dict, List, Optional
from pathlib import Path


class Database:
    """Simple file-based database for persistence."""
    
    def __init__(self, db_path: str = "data.json"):
        """Initialize database.
        
        Args:
            db_path: Path to database file
        """
        self.db_path = Path(db_path)
        self._ensure_db_exists()
    
    def _ensure_db_exists(self) -> None:
        """Ensure database file exists."""
        if not self.db_path.exists():
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self.db_path.write_text("{}", encoding="utf-8")
    
    def get(self, key: str) -> Optional[Any]:
        """Get value by key.
        
        Args:
            key: Database key
            
        Returns:
            Value if key exists, None otherwise
        """
        data = self._read()
        return data.get(key)
    
    def set(self, key: str, value: Any) -> None:
        """Set key-value pair.
        
        Args:
            key: Database key
            value: Value to store
        """
        data = self._read()
        data[key] = value
        self._write(data)
    
    def delete(self, key: str) -> bool:
        """Delete key from database.
        
        Args:
            key: Key to delete
            
        Returns:
            True if deleted, False if not found
        """
        data = self._read()
        if key in data:
            del data[key]
            self._write(data)
            return True
        return False
    
    def clear(self) -> None:
        """Clear all data from database."""
        self._write({})
    
    def _read(self) -> Dict[str, Any]:
        """Read database file.
        
        Returns:
            Dictionary of stored data
        """
        try:
            content = self.db_path.read_text(encoding="utf-8")
            return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    
    def _write(self, data: Dict[str, Any]) -> None:
        """Write data to database file.
        
        Args:
            data: Dictionary to store
        """
        self.db_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
