# This configuration is for production / docker
# You need to copy config.py.example to config.py and edit the file to your own needs
# to override these values.
PLUGINS_BUILD_DIR = "/code/plugins"
PLUGINS_REFRESH_INTERVAL_SECONDS = 12 * 60 * 60
PLUGINS_CACHE_TIMEOUT = 0  # never expire, handled by plugin refresh
# Flask automatically orders them in ascending order while
# retrieveing them. Since it is a string comparison, v10 appears before
# v2. So be careful with the ordering.
PLUGIN_VERSIONS = {
    'v1': {
        'title': '1.0',
        'response': 'The endpoints currently available for this api version' \
                ' are /api/v1/plugins and /api/v1/download',
    },
    'v2': {
        'title': '2.0',
        'response': 'The endpoints currently available for this api version' \
                ' are /api/v2/plugins, /api/v2/download and /api/v2/releases',
    },
}

# PICARD_VERSIONS dictionary valid keys are: 'stable', 'beta' and 'dev'.
# The 'version' tuple comprises int_major, int_minor, int_micro, str_type and int_development as defined in PEP-440.
# The Picard developers have standardized on using only 'dev' or 'final' as the str_type segment of the version tuple.
PICARD_VERSIONS = {
    'stable': {
        'tag': '2.8.5',
        'version': (2, 8, 5, 'final', 0),
        'urls': {
            'download': 'https://picard.musicbrainz.org/',
            'changelog': 'https://blog.metabrainz.org/2022/12/06/picard-2-8-5-released/',
        },
        'win_size': '31',
        'win_hash': '13c3e93bfa6dfcd91827450638373969',
        'win_portable_size': '44',
        'win_portable_hash': '8a00acabffb39459cff98d30424d695d',
        'mac_10_12_size': '32',
        'mac_10_12_hash': 'b02667d9d1241c80f33393fff8a2d64d',
        'mac_size': '35',
        'mac_hash': 'b80b0c5ed0cb82d567e1957b2b0c4400',
        'source_tar_size': '4.9',
        'source_tar_hash': '7bea5a3963d27ed4d069ab7dd3ac3485',
        'source_zip_size': '5.5',
        'source_zip_hash': 'dc2e5c45859950213b7e574b9050a0f6',
    },
    'beta': {
        'tag': '2.9.0b3',
        'version': (2, 9, 0, 'beta', 3),
        'urls': {
            'download': 'https://picard.musicbrainz.org/downloads/',
            'changelog': 'https://picard.musicbrainz.org/changelog/#release-2.9.0b3',
        },
        'win_size': '31',
        'win_hash': 'b7487dd8d1917a24692d62fbae9bbdcf',
        'win_portable_size': '45',
        'win_portable_hash': '2ec0811c1f2c1b54d0080bbef52db0d0',
        'mac_10_12_size': '36',
        'mac_10_12_hash': '6d8e505115d060fa0e03bcba61d510e6',
        'mac_size': '37',
        'mac_hash': 'db5ce409c75b7f7622532b33401909c9',
        'source_tar_size': '6.1',
        'source_tar_hash': 'f851821d1148af98a5f03e55e8a5d00a',
        'source_zip_size': '6.7',
        'source_zip_hash': '96d2d443ea000413b2e93e253a8647db',
    },
    'dev': {
        'tag': '2.9.0a1',
        'version': (2, 9, 0, 'alpha', 1),
        'urls': {
            'download': 'https://blog.metabrainz.org/2023/01/03/picard-2-9-alpha-1-available-for-testing/',
        }
    },
}

DOCS_BASE_URL = "https://picard-docs.musicbrainz.org"
CHANGELOG_URL = "https://raw.githubusercontent.com/musicbrainz/picard/master/NEWS.md"
CHANGELOG_CACHE_TIMEOUT = 5 * 60

SUPPORTED_LANGUAGES = [
    'en',
    'de',
    'fr',
]

SERVER_HOSTNAME = "127.0.0.1"
SERVER_PORT = 6060
SCHEDULER_API_ENABLED = True
