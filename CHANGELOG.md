# Changelog

## 2.20.1 (2026-02-10)

Full Changelog: [v2.20.0...v2.20.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.20.0...v2.20.1)

### Bug Fixes

* correct base URL to memory.papr.ai in .env.example ([d23681f](https://github.com/Papr-ai/papr-pythonSDK/commit/d23681f67468568407d7152458c62d6cdb79816a))

## 2.20.0 (2026-02-10)

Full Changelog: [v2.19.1...v2.20.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.19.1...v2.20.0)

### Features

* **api:** manual updates ([6a4fab4](https://github.com/Papr-ai/papr-pythonSDK/commit/6a4fab490a2872eec3cdf93a3b5f0f3f993c47ff))
* **api:** manual updates ([c20a236](https://github.com/Papr-ai/papr-pythonSDK/commit/c20a236fa71341ea519824cda0f4731bf0e58d8a))
* **api:** manual updates ([491cab3](https://github.com/Papr-ai/papr-pythonSDK/commit/491cab39ce4a212bdf9da51f52ec1e03253db50a))
* **api:** manual updates ([0c351dd](https://github.com/Papr-ai/papr-pythonSDK/commit/0c351dd1638877a1c4fe27e8be265c6242be6317))
* **api:** manual updates ([52ab44f](https://github.com/Papr-ai/papr-pythonSDK/commit/52ab44fb94e38c1a2d196dd76b785863f3f32453))
* **api:** manual updates ([920f87e](https://github.com/Papr-ai/papr-pythonSDK/commit/920f87e9fc172d4f97950e4dc46537cef36cb0e4))
* **client:** add custom JSON encoder for extended type support ([daf08f4](https://github.com/Papr-ai/papr-pythonSDK/commit/daf08f4a5ed93a062f4d53d923a1787a89d594b2))
* **client:** add custom JSON encoder for extended type support ([3eb2c25](https://github.com/Papr-ai/papr-pythonSDK/commit/3eb2c2543c84ec016c411f1c6659d21098191c76))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([546632c](https://github.com/Papr-ai/papr-pythonSDK/commit/546632c0978e6c664a55a5a124f8f85404faca3b))
* **docs:** fix mcp installation instructions for remote servers ([4a0a1cf](https://github.com/Papr-ai/papr-pythonSDK/commit/4a0a1cf197ffe064a51d59acb5579754354d3a20))
* resolve merge conflict issues in memory.py ([a3a59a8](https://github.com/Papr-ai/papr-pythonSDK/commit/a3a59a826ea90312f1566707a1cc7c491d72df19))
* resolve merge conflict markers in test_memory.py ([49b5cf4](https://github.com/Papr-ai/papr-pythonSDK/commit/49b5cf4dab4cd5d115c8c5987b48288afb856d83))
* resolve remaining merge conflict markers in test_schemas.py ([4ae93a1](https://github.com/Papr-ai/papr-pythonSDK/commit/4ae93a10a27adbab2509a803b1908897cbfdc5d3))


### Chores

* **internal:** version bump ([b938f88](https://github.com/Papr-ai/papr-pythonSDK/commit/b938f88561937c0bf5b53d991075e111403c4547))
* merge generated code and configure on-device dependencies ([ca16f0a](https://github.com/Papr-ai/papr-pythonSDK/commit/ca16f0a2fdc75823f8f3125bc9c559f1b4976844))


### Documentation

* add on-device processing setup guide ([c1d1b25](https://github.com/Papr-ai/papr-pythonSDK/commit/c1d1b252a4f410caf1772a5d731722c346d3491b))

## 2.19.1 (2026-01-27)

Full Changelog: [v2.19.0...v2.19.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.19.0...v2.19.1)

### Chores

* remove unused TYPE_CHECKING import ([24c4539](https://github.com/Papr-ai/papr-pythonSDK/commit/24c4539b3953e0323ac8c36a0b73c4d87f8dd9ea))

## 2.19.0 (2026-01-27)

Full Changelog: [v2.18.0...v2.19.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.18.0...v2.19.0)

### Features

* **client:** add support for binary request streaming ([31f51ee](https://github.com/Papr-ai/papr-pythonSDK/commit/31f51ee2cd3cb606576a06d1bc99c8e930148246))


### Bug Fixes

* Pydantic v2 serialization - correct __pydantic_extra__ attribute name ([bedf038](https://github.com/Papr-ai/papr-pythonSDK/commit/bedf038635e9c1c5d28748472ca87caaf9a143f4))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([a0c28f3](https://github.com/Papr-ai/papr-pythonSDK/commit/a0c28f34be7a65f66c48be665f720915e7922076))
* use async_to_httpx_files in patch method ([ca18096](https://github.com/Papr-ai/papr-pythonSDK/commit/ca1809602e6eb66e75b83ac24a782d5cda42e9de))


### Chores

* add missing docstrings ([7e29be8](https://github.com/Papr-ai/papr-pythonSDK/commit/7e29be8293e4fa86633ba5247641229c50f3b574))
* **ci:** upgrade `actions/github-script` ([a776482](https://github.com/Papr-ai/papr-pythonSDK/commit/a776482c2a66cabc1b788cfc31e64f5d5bda7bb0))
* **internal:** add `--fix` argument to lint script ([3a21ec9](https://github.com/Papr-ai/papr-pythonSDK/commit/3a21ec94d16b1dcb3ff6947dd8c759e21673191a))
* **internal:** add missing files argument to base client ([2fefc2f](https://github.com/Papr-ai/papr-pythonSDK/commit/2fefc2f0d46d81c8d3a8fbbe5d287c3aa30c0872))
* **internal:** codegen related update ([cfa5241](https://github.com/Papr-ai/papr-pythonSDK/commit/cfa52412df49e706fe33d1121d04542fbfc6fd35))
* **internal:** update `actions/checkout` version ([1314169](https://github.com/Papr-ai/papr-pythonSDK/commit/13141695db355faf3a383458f55b20ed60178beb))
* speedup initial import ([0e072e5](https://github.com/Papr-ai/papr-pythonSDK/commit/0e072e5aca0f8e9368cd19357734405b4ae89c08))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([eb9b0ec](https://github.com/Papr-ai/papr-pythonSDK/commit/eb9b0ece8188a440b994acefe89b20498db2e39c))

## 2.18.0 (2025-12-07)

Full Changelog: [v2.17.0...v2.18.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.17.0...v2.18.0)

### Features

* **api:** manual updates ([ccf1f3c](https://github.com/Papr-ai/papr-pythonSDK/commit/ccf1f3c1ae3e1d46b00d553a334b232670c2994b))
* **api:** manual updates ([a35d86e](https://github.com/Papr-ai/papr-pythonSDK/commit/a35d86e19ff0ee4c64c4538fa4e0787187969fb0))
* **api:** manual updates ([58945f0](https://github.com/Papr-ai/papr-pythonSDK/commit/58945f05d1f49aed8f618d14c905a9a6965b79b3))
* **api:** manual updates ([219753d](https://github.com/Papr-ai/papr-pythonSDK/commit/219753ddfc09d018f7b5b59982b3770b4af7632e))
* **api:** manual updates ([1e11115](https://github.com/Papr-ai/papr-pythonSDK/commit/1e111155963bf440918e0e80348fb467df2d4a28))
* **api:** manual updates ([0c51e72](https://github.com/Papr-ai/papr-pythonSDK/commit/0c51e72c22c01b90ca2713d56863dd84eb57bd0b))


### Bug Fixes

* ensure streams are always closed ([2737448](https://github.com/Papr-ai/papr-pythonSDK/commit/273744827c48c1ec7aa677ff79f83558301fe9d6))


### Chores

* add Python 3.14 classifier and testing ([3341faa](https://github.com/Papr-ai/papr-pythonSDK/commit/3341faac88c46c82dfeb3d99d4f4a998740fb194))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([0643fd8](https://github.com/Papr-ai/papr-pythonSDK/commit/0643fd82309425e225ba4e2d1baf3722806f3332))
* **docs:** use environment variables for authentication in code snippets ([b37c1bf](https://github.com/Papr-ai/papr-pythonSDK/commit/b37c1bffaf23108fc94ef06cdb4bd442589b3dd0))
* update lockfile ([6e42245](https://github.com/Papr-ai/papr-pythonSDK/commit/6e4224563b19527191623a00be769a93d7e6e6d6))

## 2.17.0 (2025-11-18)

Full Changelog: [v2.16.0...v2.17.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.16.0...v2.17.0)

### Features

* **api:** manual updates ([dfbfbc1](https://github.com/Papr-ai/papr-pythonSDK/commit/dfbfbc187b2a74bbd91ddc68508a3d6e204a0122))
* **api:** manual updates ([8a22dd2](https://github.com/Papr-ai/papr-pythonSDK/commit/8a22dd2a05d434ccbfea3f121cc025e4ecbc6e45))


### Bug Fixes

* compat with Python 3.14 ([73e782c](https://github.com/Papr-ai/papr-pythonSDK/commit/73e782c4a69301f54a3fbe4842bd415d9776b6b6))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([f679a4a](https://github.com/Papr-ai/papr-pythonSDK/commit/f679a4adbdc41a0164c3f91d5ce683f1a10c50f5))


### Chores

* **package:** drop Python 3.8 support ([b98b2b5](https://github.com/Papr-ai/papr-pythonSDK/commit/b98b2b5c893e3c49c8f47efd761d61655096dff3))

## 2.16.0 (2025-11-08)

Full Changelog: [v2.15.1...v2.16.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.15.1...v2.16.0)

### Features

* **api:** manual updates ([ed30ff4](https://github.com/Papr-ai/papr-pythonSDK/commit/ed30ff4d28b6f94c774bd624f0ea3681d3b912e2))

## 2.15.1 (2025-11-07)

Full Changelog: [v2.15.0...v2.15.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.15.0...v2.15.1)

### Bug Fixes

* resolve linting issue with import sorting ([085d1a0](https://github.com/Papr-ai/papr-pythonSDK/commit/085d1a0e8ed8055f1841ac86ee307beb8125ffcb))
* resolve type checking errors - add GraphGenerationParam import, fix NOT_GIVEN references, and handle Omit to NotGiven conversion ([c366908](https://github.com/Papr-ai/papr-pythonSDK/commit/c366908c6cff173772c9fb5b257e07cdd0461815))

## 2.15.0 (2025-11-07)

Full Changelog: [v2.14.0...v2.15.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.14.0...v2.15.0)

### Features

* **api:** manual updates ([cb73728](https://github.com/Papr-ai/papr-pythonSDK/commit/cb73728aafdf2f0d8a5fc1748b6073ef63c25441))
* **api:** manual updates ([af3d28a](https://github.com/Papr-ai/papr-pythonSDK/commit/af3d28a9af0c404ad97e52f3320c46fe0c8a5170))
* **api:** manual updates ([d5bc2a6](https://github.com/Papr-ai/papr-pythonSDK/commit/d5bc2a642e0981fe15eb746c8c1f60aa376f7d02))
* **api:** manual updates ([54bf211](https://github.com/Papr-ai/papr-pythonSDK/commit/54bf21156a92cce108f1fcccffaaf8cdbd5833df))
* **api:** manual updates ([f456d86](https://github.com/Papr-ai/papr-pythonSDK/commit/f456d86dc8d97ec9e8e6ee0ea49b2ee13d66e224))
* **api:** manual updates ([f72c22b](https://github.com/Papr-ai/papr-pythonSDK/commit/f72c22bc4b7fef6127d957264bfd0d567cfe4ed1))


### Bug Fixes

* **client:** close streams without requiring full consumption ([60d5c8d](https://github.com/Papr-ai/papr-pythonSDK/commit/60d5c8d4876dcc73b4131c9259612ba85d2cc5a8))
* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([a8ce491](https://github.com/Papr-ai/papr-pythonSDK/commit/a8ce491375ac71e81243ea95116db88d968d20df))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([6ad9ac3](https://github.com/Papr-ai/papr-pythonSDK/commit/6ad9ac3f9e7ab2ce1f021ac773659f56b66a6e61))
* do not install brew dependencies in ./scripts/bootstrap by default ([8933182](https://github.com/Papr-ai/papr-pythonSDK/commit/8933182759f18e3b007985e1054f3af66d8a0b4f))
* improve example values ([4a251d9](https://github.com/Papr-ai/papr-pythonSDK/commit/4a251d91445218a65beda3f1850f90793be5fbfb))
* **internal/tests:** avoid race condition with implicit client cleanup ([1ff59e8](https://github.com/Papr-ai/papr-pythonSDK/commit/1ff59e898f1f966e6e740c3831c73a471c1780d2))
* **internal:** detect missing future annotations with ruff ([22c7240](https://github.com/Papr-ai/papr-pythonSDK/commit/22c7240a5f69127c14cfa279fe17f4df3c3fea5c))
* **internal:** move mypy configurations to `pyproject.toml` file ([2919d5c](https://github.com/Papr-ai/papr-pythonSDK/commit/2919d5c0e5c5861b86d865fbafd63098cf6ad3ff))
* **internal:** update pydantic dependency ([8bf7777](https://github.com/Papr-ai/papr-pythonSDK/commit/8bf7777e5ad4afaf74a8db90713efc28f1f88bf0))
* **tests:** simplify `get_platform` test ([5e0cb1f](https://github.com/Papr-ai/papr-pythonSDK/commit/5e0cb1f4fc3c255682f672deb7cad924153880df))
* **types:** change optional parameter type from NotGiven to Omit ([f5e71dc](https://github.com/Papr-ai/papr-pythonSDK/commit/f5e71dca2a1ee9ec7ea90f3f4b75eb7eaafd120d))

## 2.14.0 (2025-09-04)

Full Changelog: [v2.13.0...v2.14.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.13.0...v2.14.0)

### Features

* **api:** update via SDK Studio ([79dd58f](https://github.com/Papr-ai/papr-pythonSDK/commit/79dd58f9a14dfd5ddf171301ad3ed24160a1f732))
* improve future compat with pydantic v3 ([e21a0d2](https://github.com/Papr-ai/papr-pythonSDK/commit/e21a0d23054cca94cfe021b778fb51621cd909af))
* **types:** replace List[str] with SequenceNotStr in params ([8e1ae65](https://github.com/Papr-ai/papr-pythonSDK/commit/8e1ae65be9355332e94f179b1af4668ea870272c))

## 2.13.0 (2025-09-02)

Full Changelog: [v2.12.0...v2.13.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.12.0...v2.13.0)

### Features

* **api:** update via SDK Studio ([244911a](https://github.com/Papr-ai/papr-pythonSDK/commit/244911aa37a5f703d054f8e5ce9ebeb12c84d077))
* **api:** update via SDK Studio ([c115860](https://github.com/Papr-ai/papr-pythonSDK/commit/c115860dabf279d449e20e27cd39f500c70a5381))
* **api:** update via SDK Studio ([9697a29](https://github.com/Papr-ai/papr-pythonSDK/commit/9697a2981f2f55d2f5e82140af78ccef0061222a))
* **api:** update via SDK Studio ([41abf8f](https://github.com/Papr-ai/papr-pythonSDK/commit/41abf8fdb91495a1a7c04a3030b99d9a7f85920e))
* **api:** update via SDK Studio ([306cbe4](https://github.com/Papr-ai/papr-pythonSDK/commit/306cbe43a567f95766fec227c181f17460c8f3de))


### Bug Fixes

* avoid newer type syntax ([7484544](https://github.com/Papr-ai/papr-pythonSDK/commit/748454411bad211e97f76486a92e9b36d4fdc2f8))


### Chores

* **internal:** add Sequence related utils ([0df267f](https://github.com/Papr-ai/papr-pythonSDK/commit/0df267f10a16f5ba78f95263b76dff0376126a1c))
* **internal:** change ci workflow machines ([c12d198](https://github.com/Papr-ai/papr-pythonSDK/commit/c12d19804a98f31470ab339eb4215074fa9076e2))
* **internal:** codegen related update ([ca29229](https://github.com/Papr-ai/papr-pythonSDK/commit/ca29229f32dbc907761eb9673fc9ff3d5088d0f0))
* **internal:** fix ruff target version ([ba4b4ca](https://github.com/Papr-ai/papr-pythonSDK/commit/ba4b4ca53e18bb02d18509d9ae31f3955b4dd855))
* **internal:** update comment in script ([6edd9d6](https://github.com/Papr-ai/papr-pythonSDK/commit/6edd9d684c409b0750cb8446b83d25342c5af1b0))
* **internal:** update pyright exclude list ([2cfcb03](https://github.com/Papr-ai/papr-pythonSDK/commit/2cfcb030270485009be6bd019b444070529690ba))
* update @stainless-api/prism-cli to v5.15.0 ([a07b404](https://github.com/Papr-ai/papr-pythonSDK/commit/a07b404e75304a1e7427521fac583ef8664aba10))
* update github action ([3737e5a](https://github.com/Papr-ai/papr-pythonSDK/commit/3737e5a8d1bb51d5d59d5f26081db5dcc0951f90))

## 2.12.0 (2025-07-31)

Full Changelog: [v2.11.0...v2.12.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.11.0...v2.12.0)

### Features

* **api:** update via SDK Studio ([d95b3b5](https://github.com/Papr-ai/papr-pythonSDK/commit/d95b3b544c8fb2f9a626616f88ba9f71ee8b6f7e))
* **client:** support file upload requests ([d3ae699](https://github.com/Papr-ai/papr-pythonSDK/commit/d3ae699a5f01ac1994e34b57f4296f66b0365102))


### Bug Fixes

* **parsing:** ignore empty metadata ([a9d9108](https://github.com/Papr-ai/papr-pythonSDK/commit/a9d9108b3ee0c7c7b413d0ffdc6ec69398f4fa5c))
* **parsing:** parse extra field types ([dacefad](https://github.com/Papr-ai/papr-pythonSDK/commit/dacefada6822225d1ccfd25f246a46f8b1fb4c87))


### Chores

* **project:** add settings file for vscode ([142267f](https://github.com/Papr-ai/papr-pythonSDK/commit/142267f3e7425c8a799c8170729ffb5098d66eec))

## 2.11.0 (2025-07-15)

Full Changelog: [v2.10.2...v2.11.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.10.2...v2.11.0)

### Features

* **api:** update via SDK Studio ([f282df5](https://github.com/Papr-ai/papr-pythonSDK/commit/f282df57b3ead80cad000398a24dfcb7125ff89f))
* **api:** update via SDK Studio ([b5a3798](https://github.com/Papr-ai/papr-pythonSDK/commit/b5a37989bf9615c0a496d2aaa682a170a40c7dd2))
* **api:** update via SDK Studio ([5a3924b](https://github.com/Papr-ai/papr-pythonSDK/commit/5a3924bac22765c8aa5d416ab24d482274334528))
* **api:** update via SDK Studio ([cad8b8f](https://github.com/Papr-ai/papr-pythonSDK/commit/cad8b8fe78799db26a9be488a613a10d3a410e7a))
* clean up environment call outs ([1737742](https://github.com/Papr-ai/papr-pythonSDK/commit/1737742dcbdb6b745e593399f54bbd9dde719e85))

## 2.10.2 (2025-07-12)

Full Changelog: [v2.10.1...v2.10.2](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.10.1...v2.10.2)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([475b53d](https://github.com/Papr-ai/papr-pythonSDK/commit/475b53d22749304c6971e1f02bf3834b5bfddcd1))


### Chores

* **internal:** codegen related update ([48e3664](https://github.com/Papr-ai/papr-pythonSDK/commit/48e36649fcf44aa333a16716fde4b9c843f137ef))
* **internal:** codegen related update ([e3852da](https://github.com/Papr-ai/papr-pythonSDK/commit/e3852daf09e2149a55954f87747dd8e5e9193510))
* **readme:** fix version rendering on pypi ([8b2b2fb](https://github.com/Papr-ai/papr-pythonSDK/commit/8b2b2fbf22126bd801d36f757b820662d75bff32))

## 2.10.1 (2025-07-10)

Full Changelog: [v2.10.0...v2.10.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.10.0...v2.10.1)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([2cd20c8](https://github.com/Papr-ai/papr-pythonSDK/commit/2cd20c8e3d568bf6aaa11aa39e26100a4e338d09))


### Chores

* **package:** mark python 3.13 as supported ([9c3d58e](https://github.com/Papr-ai/papr-pythonSDK/commit/9c3d58e42a0f5a7a6ab6dd7d2f58e39fa7969fbc))

## 2.10.0 (2025-07-09)

Full Changelog: [v2.9.0...v2.10.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.9.0...v2.10.0)

### Features

* **api:** update via SDK Studio ([6a68fa9](https://github.com/Papr-ai/papr-pythonSDK/commit/6a68fa9c4f5119b9d295d689bec3850e8f1b8c02))
* **api:** update via SDK Studio ([e7b4b45](https://github.com/Papr-ai/papr-pythonSDK/commit/e7b4b45f1524dd4a7376216c4fe50a36895478c0))


### Chores

* **ci:** change upload type ([eee0262](https://github.com/Papr-ai/papr-pythonSDK/commit/eee026256d9592a4eb716b99c41f0f2870462191))
* **internal:** bump pinned h11 dep ([256411e](https://github.com/Papr-ai/papr-pythonSDK/commit/256411e069cd28390d59a61d9ea338a0d823df3f))

## 2.9.0 (2025-06-30)

Full Changelog: [v2.8.1...v2.9.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.8.1...v2.9.0)

### Features

* **api:** update via SDK Studio ([1fa717e](https://github.com/Papr-ai/papr-pythonSDK/commit/1fa717e48c6305c2c4c49f18722e95a31266c339))

## 2.8.1 (2025-06-30)

Full Changelog: [v2.8.0...v2.8.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.8.0...v2.8.1)

### Bug Fixes

* **ci:** correct conditional ([9e3bfd1](https://github.com/Papr-ai/papr-pythonSDK/commit/9e3bfd14dbe6018999a1a22ffff8ac84a673957c))


### Chores

* **ci:** only run for pushes and fork pull requests ([406912e](https://github.com/Papr-ai/papr-pythonSDK/commit/406912eb3d2d92403d66d511771087705e61a163))

## 2.8.0 (2025-06-27)

Full Changelog: [v2.7.0...v2.8.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.7.0...v2.8.0)

### Features

* **client:** add support for aiohttp ([e8ea941](https://github.com/Papr-ai/papr-pythonSDK/commit/e8ea941c4f3b3fca4b5d3c8a9355a0ce9c9dd92b))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([cd2d26b](https://github.com/Papr-ai/papr-pythonSDK/commit/cd2d26be6032e09b380ab46efe4bfe67f08b4690))


### Chores

* **tests:** skip some failing tests on the latest python versions ([ff00e9a](https://github.com/Papr-ai/papr-pythonSDK/commit/ff00e9a33cc668c04875a22f7980c82235373e90))

## 2.7.0 (2025-06-19)

Full Changelog: [v2.6.2...v2.7.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.6.2...v2.7.0)

### Features

* **api:** update via SDK Studio ([994c0a4](https://github.com/Papr-ai/papr-pythonSDK/commit/994c0a421b63de3288db729bfcbf1cc31e302615))

## 2.6.2 (2025-06-19)

Full Changelog: [v2.6.1...v2.6.2](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.6.1...v2.6.2)

### Documentation

* **client:** fix httpx.Timeout documentation reference ([ca31f17](https://github.com/Papr-ai/papr-pythonSDK/commit/ca31f172bbc9d054a3400f2fc50e4c2639f17a46))

## 2.6.1 (2025-06-18)

Full Changelog: [v2.6.0...v2.6.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.6.0...v2.6.1)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([6c2abba](https://github.com/Papr-ai/papr-pythonSDK/commit/6c2abbae26a7da899e4c73606197485d50349e3a))


### Chores

* **readme:** update badges ([1dd9392](https://github.com/Papr-ai/papr-pythonSDK/commit/1dd93927116479e91960234c04e7bf72eff32444))

## 2.6.0 (2025-06-17)

Full Changelog: [v2.5.0...v2.6.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.5.0...v2.6.0)

### Features

* **api:** update via SDK Studio ([66558c4](https://github.com/Papr-ai/papr-pythonSDK/commit/66558c421ab198628831947858d224280c299ad9))


### Chores

* **ci:** enable for pull requests ([7f7e6c5](https://github.com/Papr-ai/papr-pythonSDK/commit/7f7e6c52ede6a229780741ac401f74a71e26adac))
* **internal:** update conftest.py ([2a36c9b](https://github.com/Papr-ai/papr-pythonSDK/commit/2a36c9b4fc019b48aaf8a2da4d71421fe1f088e2))
* **tests:** add tests for httpx client instantiation & proxies ([1d6ed96](https://github.com/Papr-ai/papr-pythonSDK/commit/1d6ed963119ab35164818c5d2b2af2451fcbe9ac))

## 2.5.0 (2025-06-13)

Full Changelog: [v2.4.0...v2.5.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.4.0...v2.5.0)

### Features

* **api:** update via SDK Studio ([fd1bab0](https://github.com/Papr-ai/papr-pythonSDK/commit/fd1bab09d566859a11bd6021121094640bec3814))

## 2.4.0 (2025-06-13)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.3.0...v2.4.0)

### Features

* **api:** update via SDK Studio ([ba10eec](https://github.com/Papr-ai/papr-pythonSDK/commit/ba10eec0af063ad741af0587dffb13cf5dde3b03))
* **client:** add follow_redirects request option ([4577c2e](https://github.com/Papr-ai/papr-pythonSDK/commit/4577c2e8287c951b898750a9ced105509aba7932))


### Bug Fixes

* **client:** correctly parse binary response | stream ([0099bdf](https://github.com/Papr-ai/papr-pythonSDK/commit/0099bdf924204499dffe06cbe61b99d1bea0323a))


### Chores

* **ci:** fix installation instructions ([a603af0](https://github.com/Papr-ai/papr-pythonSDK/commit/a603af04ae32f18947e815ebac9b7d0d2d8e9a37))
* **docs:** grammar improvements ([dffdbe6](https://github.com/Papr-ai/papr-pythonSDK/commit/dffdbe6b3113736f9ce175956d2bc1875c97d5bf))
* **docs:** remove reference to rye shell ([581d32b](https://github.com/Papr-ai/papr-pythonSDK/commit/581d32ba64ba96b359edb40cc85842b3eb0c9048))
* **docs:** remove unnecessary param examples ([e37fd8c](https://github.com/Papr-ai/papr-pythonSDK/commit/e37fd8c11691838dcb3aee45865afcde0df5432e))
* **tests:** run tests in parallel ([fad0271](https://github.com/Papr-ai/papr-pythonSDK/commit/fad02716979bf41b5ce16733622d3e77e17b7a26))

## 2.3.0 (2025-05-15)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.2.0...v2.3.0)

### Features

* **api:** update via SDK Studio ([37485dc](https://github.com/Papr-ai/papr-pythonSDK/commit/37485dc7c6c11f393bbe51fc01fecba57b1f4263))

## 2.2.0 (2025-05-15)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.1.0...v2.2.0)

### Features

* **api:** update via SDK Studio ([22fdd47](https://github.com/Papr-ai/papr-pythonSDK/commit/22fdd4724acf31388c32e9eedf49b648f8e6f3cb))

## 2.1.0 (2025-05-15)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v2.0.0...v2.1.0)

### Features

* **api:** update via SDK Studio ([0097341](https://github.com/Papr-ai/papr-pythonSDK/commit/00973418345ab68f6679ae171d4eb4ef6d227635))


### Chores

* **ci:** upload sdks to package manager ([c4a449a](https://github.com/Papr-ai/papr-pythonSDK/commit/c4a449ac84a69d1b11d9d140b6ae8a2f5bb39385))

## 2.0.0 (2025-05-14)

Full Changelog: [v1.0.1...v2.0.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v1.0.1...v2.0.0)

### Features

* **api:** update via SDK Studio ([9c116ef](https://github.com/Papr-ai/papr-pythonSDK/commit/9c116ef0c678cc8025037fe06ce52e5bbbb84c07))
* **api:** update via SDK Studio ([95f4f78](https://github.com/Papr-ai/papr-pythonSDK/commit/95f4f78d234f96e3be0fa19aa0e1fd53ef3bf5eb))


### Chores

* update SDK settings ([448185c](https://github.com/Papr-ai/papr-pythonSDK/commit/448185cd5236c4dbeca3d016e95594886b12c24f))

## 1.0.1 (2025-05-14)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/Papr-ai/papr-pythonSDK/compare/v1.0.0...v1.0.1)

### Chores

* update SDK settings ([2215a2e](https://github.com/Papr-ai/papr-pythonSDK/commit/2215a2e2cad17a560707314ba43ecdbe4b2aaf68))

## 1.0.0 (2025-05-14)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/Papr-ai/papr-pythonSDK/compare/v0.0.1-alpha.0...v1.0.0)

### Features

* **api:** update via SDK Studio ([7856824](https://github.com/Papr-ai/papr-pythonSDK/commit/78568240285cad273dab70588033260486856539))
* **api:** update via SDK Studio ([b1aaec6](https://github.com/Papr-ai/papr-pythonSDK/commit/b1aaec6d2c0d02d2f9bbb936318a9b420d932ae8))


### Chores

* update SDK settings ([dc4e8e7](https://github.com/Papr-ai/papr-pythonSDK/commit/dc4e8e7c0fe118d94f10b3ecd0b110ba87e53341))
* update SDK settings ([d150fb5](https://github.com/Papr-ai/papr-pythonSDK/commit/d150fb554a92e69c4a33d280155fbf7419fc160a))
