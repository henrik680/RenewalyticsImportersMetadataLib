import json


def importer_metadata(content_description, input_json, path_url, project_name, language, source):
    # Function used to collect metadata for a Renewalytics GCP Storage bucket.
    if input_json.get('metadata') is None:
        metadata = {}
    else:
        metadata = json.loads(input_json.get('metadata'))
    metadata['code_module'] = project_name
    metadata['content_description'] = content_description
    metadata['data_path_url'] = path_url
    metadata['language'] = language
    metadata['source'] = source     # Wikipedia / Company webpage / Government Agency webpage / Market webpage
    return metadata
