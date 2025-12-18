import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # 1. IP address in URL
    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        features.append(-1)
    else:
        features.append(1)

    # 2. URL length
    if len(url) > 54:
        features.append(1)
    else:
        features.append(-1)

    # 3. '@' symbol
    if '@' in url:
        features.append(-1)
    else:
        features.append(1)

    # 4. Prefix or suffix '-'
    domain = urlparse(url).netloc
    if '-' in domain:
        features.append(-1)
    else:
        features.append(1)

    # 5. HTTPS token
    if 'https' in url and not url.startswith('https'):
        features.append(-1)
    else:
        features.append(1)

    return features
