#!/usr/bin/env python3
"""
Ontology Manager - Knowledge Graph Operations
"""

import json
import os
from datetime import datetime

ONTOLOGY_FILE = "ontology_data.json"

class OntologyManager:
    def __init__(self):
        self.data = self._load()
    
    def _load(self):
        if os.path.exists(ONTOLOGY_FILE):
            with open(ONTOLOGY_FILE, 'r') as f:
                return json.load(f)
        return {"entities": {}, "relations": []}
    
    def _save(self):
        with open(ONTOLOGY_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def create_entity(self, entity_type, name, properties=None):
        """Create a new entity"""
        entity_id = f"{entity_type}_{name}_{datetime.now().timestamp()}"
        entity = {
            "id": entity_id,
            "type": entity_type,
            "name": name,
            "properties": properties or {},
            "created": datetime.now().isoformat()
        }
        self.data["entities"][entity_id] = entity
        self._save()
        return entity_id
    
    def get_entity(self, entity_id):
        """Get an entity by ID"""
        return self.data["entities"].get(entity_id)
    
    def link_entities(self, from_id, to_id, relation_type):
        """Create a relation between entities"""
        relation = {
            "from": from_id,
            "to": to_id,
            "type": relation_type,
            "created": datetime.now().isoformat()
        }
        self.data["relations"].append(relation)
        self._save()
        return relation
    
    def query_entities(self, entity_type=None, **filters):
        """Query entities by type and properties"""
        results = []
        for entity in self.data["entities"].values():
            if entity_type and entity["type"] != entity_type:
                continue
            match = all(entity["properties"].get(k) == v for k, v in filters.items())
            if match:
                results.append(entity)
        return results

if __name__ == "__main__":
    import sys
    manager = OntologyManager()
    
    command = sys.argv[1] if len(sys.argv) > 1 else "list"
    
    if command == "create" and len(sys.argv) > 3:
        entity_id = manager.create_entity(sys.argv[2], sys.argv[3])
        print(f"Created entity: {entity_id}")
    elif command == "get" and len(sys.argv) > 2:
        print(json.dumps(manager.get_entity(sys.argv[2]), indent=2))
    elif command == "list":
        print(json.dumps(manager.data["entities"], indent=2))