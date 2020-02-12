"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import psycopg2
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


class DWFDB:
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                host=settings.POSTGRES_HOST_NAME,
                port=settings.POSTGRES_PORT,
                database=settings.POSTGRES_DB_NAME,
            )

        except Exception as error:
            self.connection = None
            logger.error("Error while connecting to PostgreSQL: ", error)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            # closing database connection.
            if self.connection:
                self.connection.close()
        except Exception as ex:
            logger.error("Exception while closing connection: ", ex)
            try:
                self.connection.close()
            except Exception as exp:
                logger.error("Error while closing to PostgreSQL Connection: ", exp)
        finally:
            self.connection = None
