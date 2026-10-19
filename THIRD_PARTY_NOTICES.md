# Third-Party Notices

Project Delphi uses third-party software components. These components remain
under their own licenses.

## Bundled frontend runtime

`vendor/papyros/runtime.mjs` bundles Papyros and its frontend dependencies from
npm. Complete contributing-package license texts are retained in
`vendor/papyros/LICENSES.txt`, with additional source license comments in
`vendor/papyros/runtime.mjs.LEGAL.txt`. Exact package versions and the bundle hash
are recorded in `vendor/papyros/provenance.json`. The reproducible build and lock
file are in `tools/papyros-runtime/`; original package sources remain available
through the npm package URLs recorded in that lock file.

## Papyros

- Component: `@dodona/papyros`
- Copyright: Copyright (c) 2021 Dodona
- License: MIT License
- Sources:
  - https://www.npmjs.com/package/%40dodona/papyros
  - https://github.com/dodona-edu/papyros
  - https://docs.dodona.be/papyros/

### MIT License text (Papyros)

MIT License

Copyright (c) 2021 Dodona

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
