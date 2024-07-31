
## Logging

Remember to import the logger in any other files where you want to add logging. You can do this by adding:
```py
from app.utils.logger import setup_logger
logger = setup_logger(__name__)
```
at the top of the file, and then use logger.info(), logger.warning(), logger.error(), etc. as needed.
