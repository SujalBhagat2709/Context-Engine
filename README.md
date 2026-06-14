# Context Engine

## Overview

Context Engine stores, updates, and retrieves context information that can influence future decisions and responses.

---

## Features

- Persistent Context
- Context Updates
- Context Retrieval
- JSON Storage

---

## Files

- context_manager.py
- context_processor.py

---

## Usage

```bash
python context_processor.py
```

---

## Example

Store Context:

```text
name = Sujal
```

Output:

```text
✓ Context Updated
```

Store Another Context:

```text
skill = Python
```

Output:

```text
✓ Context Updated
```

Retrieve Context:

```text
name
```

Output:

```text
Sujal
```

Show All Context:

```text
show
```

Output:

```text
name: Sujal
skill: Python
```

---

## Future Improvements

- Context Relationships
- Session Context
- Agent Context
- Smart Recommendations
- Context Priorities
- Knowledge Graph Integration