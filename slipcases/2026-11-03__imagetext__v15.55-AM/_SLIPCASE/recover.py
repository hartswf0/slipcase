import base64, io, pathlib, re, sys, zipfile
source, dest = map(pathlib.Path, sys.argv[1:3])
data = re.search(r'<script id="rebuild-kit" type="application/octet-stream">([A-Za-z0-9+/=]+)</script>',source.read_text()).group(1)
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(io.BytesIO(base64.b64decode(data))) as z:
    assert z.testzip() is None
    for name in z.namelist():
        assert not pathlib.PurePosixPath(name).is_absolute() and '..' not in pathlib.PurePosixPath(name).parts
    z.extractall(dest)
(dest/'index.html').write_bytes(source.read_bytes())
