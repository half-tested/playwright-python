import hashlib
import os

import allure
import pytest
from slugify import slugify


@pytest.fixture(scope='function', autouse=True)
def add_artifacts_to_allure_teardown(request):
    yield

    output_dir = request.config.getoption("--output")
    output_path = os.path.join(output_dir, truncate_file_name(slugify(request.node.nodeid)))

    ext = ("png", "webm", "zip")
    if not os.path.exists(output_path):
        return
    for file in os.listdir(output_path):
        if file.endswith(ext):
            allure.attach(
                open(os.path.join(output_path, file), 'rb').read(),
                name=f"{file}",
                extension=file.split('.')[-1]
            )


def truncate_file_name(file_name: str) -> str:
    if len(file_name) < 256:
        return file_name
    return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"
