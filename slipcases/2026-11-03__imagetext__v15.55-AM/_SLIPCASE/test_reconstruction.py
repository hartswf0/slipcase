import hashlib, json, pathlib, subprocess, sys, tempfile, zipfile
archive, capsule = map(pathlib.Path, sys.argv[1:3])
with tempfile.TemporaryDirectory() as t, zipfile.ZipFile(archive) as z:
    dst=pathlib.Path(t)/'restored'
    helper=pathlib.Path(t)/'recover.py'
    helper.write_bytes(z.read('_SLIPCASE/recover.py'))
    subprocess.run([sys.executable,str(helper),str(capsule),str(dst)],check=True)
    assert z.testzip() is None
    assert set(z.namelist())=={str(p.relative_to(dst)) for p in dst.rglob('*') if p.is_file()}
    for n in z.namelist(): assert (dst/n).read_bytes()==z.read(n), n
    print(f'ZIP CRC and isolated capsule rebuild verified for {len(z.namelist())} members')
    m=json.loads((dst/'_SLIPCASE/MANIFEST.json').read_text())
    for n,h in m['hashes'].items(): assert hashlib.sha256((dst/n).read_bytes()).hexdigest()==h,n
    print(f'Manifest hashes verified for {len(m["hashes"])} members')
