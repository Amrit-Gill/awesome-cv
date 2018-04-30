#!/usr/bin/env python3

import connexion
import logging
import logging.config
import encoder


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("Starting awesome cv backend")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Awesome CV backend'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
