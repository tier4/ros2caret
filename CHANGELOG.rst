^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros2caret
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.5.0 (2024-02-06)
------------------
* refactor: change the version management method (`#169 <https://github.com/tier4/ros2caret/issues/169>`_)
  * Update: method of get version
  * Update: Change in version control method
  * Fix: not use codecs
  * Fix: change how to specify path
  * Fix: path name
  ---------
* fix: ignore caret package on workflow pytest (`#170 <https://github.com/tier4/ros2caret/issues/170>`_)
  * Fix: repository name
  * Not install caret packages registered in buildfarm
  * Fix: unknown word
  * Fix: change ignore method
  * Revert "Revert: repository name"
  This reverts commit 3735506cf074970a047686e00bdeb91f049e30c0.
  * Update .github/workflows/pytest.yaml
  Co-authored-by: ymski <yamasaki@isp.co.jp>
  ---------
  Co-authored-by: ymski <yamasaki@isp.co.jp>
* Update: package.xml version to 0.4.24 (`#167 <https://github.com/tier4/ros2caret/issues/167>`_)
* ci(pre-commit): autoupdate (`#166 <https://github.com/tier4/ros2caret/issues/166>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.38.0 → v0.39.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.38.0...v0.39.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.24 (`#165 <https://github.com/tier4/ros2caret/issues/165>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* fix: support environment without std::input to stop recording (`#164 <https://github.com/tier4/ros2caret/issues/164>`_)
  * fix: support environment without std::input to stop recording
  * fix flake8
  ---------
* chore: update version to v0.4.23 (`#162 <https://github.com/tier4/ros2caret/issues/162>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* refactor: improvement of ros distribution determination method (`#161 <https://github.com/tier4/ros2caret/issues/161>`_)
  * refactor: improvement of judgement ros distribution
  * chore: fix log message
  * chore: fix comment message
  * fix: modify comment
  ---------
* fix(check_caret_rclcpp): skip check_caret_rclcpp for ROS Distributions after iron (`#135 <https://github.com/tier4/ros2caret/issues/135>`_)
  * fix(check_caret_rclcpp): skip check_caret_rclcpp for ROS Distributions after iron
  * refactor: fix log message
  * fix typo
  * fix style
  * add test
  * modify message
  * style
  ---------
* ci(pre-commit): autoupdate (`#160 <https://github.com/tier4/ros2caret/issues/160>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v4.0.0-alpha.4 → v4.0.0-alpha.8](https://github.com/pre-commit/mirrors-prettier/compare/v4.0.0-alpha.4...v4.0.0-alpha.8)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* refactor: upgrade xml version (`#159 <https://github.com/tier4/ros2caret/issues/159>`_)
* chore: update version to v0.4.22 (`#158 <https://github.com/tier4/ros2caret/issues/158>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#157 <https://github.com/tier4/ros2caret/issues/157>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.37.0 → v0.38.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.37.0...v0.38.0)
  - [github.com/pre-commit/mirrors-prettier: v3.1.0 → v4.0.0-alpha.4](https://github.com/pre-commit/mirrors-prettier/compare/v3.1.0...v4.0.0-alpha.4)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* Enable sim_time trace point in light mode. (`#152 <https://github.com/tier4/ros2caret/issues/152>`_)
* ci(pre-commit): autoupdate (`#156 <https://github.com/tier4/ros2caret/issues/156>`_)
  updates:
  - [github.com/scop/pre-commit-shfmt: v3.7.0-3 → v3.7.0-4](https://github.com/scop/pre-commit-shfmt/compare/v3.7.0-3...v3.7.0-4)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.21 (`#155 <https://github.com/tier4/ros2caret/issues/155>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#153 <https://github.com/tier4/ros2caret/issues/153>`_)
  updates:
  - [github.com/scop/pre-commit-shfmt: v3.7.0-2 → v3.7.0-3](https://github.com/scop/pre-commit-shfmt/compare/v3.7.0-2...v3.7.0-3)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#148 <https://github.com/tier4/ros2caret/issues/148>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: update version to v0.4.20 (`#149 <https://github.com/tier4/ros2caret/issues/149>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore: sync files (`#151 <https://github.com/tier4/ros2caret/issues/151>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#150 <https://github.com/tier4/ros2caret/issues/150>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.3 → v3.1.0](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.3...v3.1.0)
  - [github.com/adrienverge/yamllint: v1.32.0 → v1.33.0](https://github.com/adrienverge/yamllint/compare/v1.32.0...v1.33.0)
  - [github.com/scop/pre-commit-shfmt: v3.7.0-1 → v3.7.0-2](https://github.com/scop/pre-commit-shfmt/compare/v3.7.0-1...v3.7.0-2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update maintainer (`#143 <https://github.com/tier4/ros2caret/issues/143>`_)
  * chore: update maintainer
  * update setup.py
  ---------
* chore: sync files (`#147 <https://github.com/tier4/ros2caret/issues/147>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#146 <https://github.com/tier4/ros2caret/issues/146>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#145 <https://github.com/tier4/ros2caret/issues/145>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#144 <https://github.com/tier4/ros2caret/issues/144>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#142 <https://github.com/tier4/ros2caret/issues/142>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#141 <https://github.com/tier4/ros2caret/issues/141>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#140 <https://github.com/tier4/ros2caret/issues/140>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#138 <https://github.com/tier4/ros2caret/issues/138>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#139 <https://github.com/tier4/ros2caret/issues/139>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#137 <https://github.com/tier4/ros2caret/issues/137>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#133 <https://github.com/tier4/ros2caret/issues/133>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore: update version to v0.4.19 (`#136 <https://github.com/tier4/ros2caret/issues/136>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#134 <https://github.com/tier4/ros2caret/issues/134>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* refactor: remove -d for ros2 caret command  (`#129 <https://github.com/tier4/ros2caret/issues/129>`_)
  * refactor: remove -d from ros2 caret command
  * fix: flake8 error
  * refactor: remove -w for ros2 caret command
  ---------
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#132 <https://github.com/tier4/ros2caret/issues/132>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#131 <https://github.com/tier4/ros2caret/issues/131>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#130 <https://github.com/tier4/ros2caret/issues/130>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#127 <https://github.com/tier4/ros2caret/issues/127>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#128 <https://github.com/tier4/ros2caret/issues/128>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* feat: add record-clock option (`#125 <https://github.com/tier4/ros2caret/issues/125>`_)
  * feat: add record-clock option
  * fix: change to not using shell
  * fix
  * fix: change the way the process is killed
  * chore: ignore cspell
  * fix: pass pytest
  * fix
  * fix
  ---------
* chore: update version to v0.4.18 (`#126 <https://github.com/tier4/ros2caret/issues/126>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#120 <https://github.com/tier4/ros2caret/issues/120>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* add option for recording immediately (`#123 <https://github.com/tier4/ros2caret/issues/123>`_)
* ci(pre-commit): autoupdate (`#124 <https://github.com/tier4/ros2caret/issues/124>`_)
  updates:
  - [github.com/pre-commit/pre-commit-hooks: v4.4.0 → v4.5.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.4.0...v4.5.0)
  - [github.com/AleksaC/hadolint-py: v2.12.0.2 → v2.12.0.3](https://github.com/AleksaC/hadolint-py/compare/v2.12.0.2...v2.12.0.3)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* feat: support light mode for iron (`#86 <https://github.com/tier4/ros2caret/issues/86>`_)
  * pass test
  * fix wrong import order
  * update event_ust list
  * add whitespace
  ---------
* feat: support subbuffer size option (`#85 <https://github.com/tier4/ros2caret/issues/85>`_)
  * add append arg
  * delete blank lines
  * pass test
  * fix wrong import order
  * add ros2_tracing copyright
  * fix comment for copyright
  * fix comment for copyright
  * fix link (rolling to humble)
  * add option for subbuffer_size
  * add subbuffer_size arg
  * add some exception
  * fix wrong import order
  * remove numpy dependency
  * Update ros2caret/verb/caret_record_init.py
  Co-authored-by: isp-uetsuki <35490433+isp-uetsuki@users.noreply.github.com>
  * change to the method of determining powers of 2 using bitwise operations
  ---------
  Co-authored-by: isp-uetsuki <35490433+isp-uetsuki@users.noreply.github.com>
* feat: support non-optional argument `append-trace` (`#84 <https://github.com/tier4/ros2caret/issues/84>`_)
  * add append arg
  * delete blank lines
  * pass test
  * fix wrong import order
  * add ros2_tracing copyright
  * fix comment for copyright
  * fix comment for copyright
  * fix link (rolling to humble)
  ---------
* chore: update version to v0.4.17 (`#122 <https://github.com/tier4/ros2caret/issues/122>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#121 <https://github.com/tier4/ros2caret/issues/121>`_)
  updates:
  - [github.com/shellcheck-py/shellcheck-py: v0.9.0.5 → v0.9.0.6](https://github.com/shellcheck-py/shellcheck-py/compare/v0.9.0.5...v0.9.0.6)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#119 <https://github.com/tier4/ros2caret/issues/119>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#118 <https://github.com/tier4/ros2caret/issues/118>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#117 <https://github.com/tier4/ros2caret/issues/117>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#116 <https://github.com/tier4/ros2caret/issues/116>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#115 <https://github.com/tier4/ros2caret/issues/115>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.36.0 → v0.37.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.36.0...v0.37.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#114 <https://github.com/tier4/ros2caret/issues/114>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#113 <https://github.com/tier4/ros2caret/issues/113>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#112 <https://github.com/tier4/ros2caret/issues/112>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore: sync files (`#110 <https://github.com/tier4/ros2caret/issues/110>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#111 <https://github.com/tier4/ros2caret/issues/111>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: update version to v0.4.16.1 (`#109 <https://github.com/tier4/ros2caret/issues/109>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#108 <https://github.com/tier4/ros2caret/issues/108>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: update version to v0.4.16 (`#107 <https://github.com/tier4/ros2caret/issues/107>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore: sync files (`#106 <https://github.com/tier4/ros2caret/issues/106>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#105 <https://github.com/tier4/ros2caret/issues/105>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#104 <https://github.com/tier4/ros2caret/issues/104>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#103 <https://github.com/tier4/ros2caret/issues/103>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#102 <https://github.com/tier4/ros2caret/issues/102>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#101 <https://github.com/tier4/ros2caret/issues/101>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#100 <https://github.com/tier4/ros2caret/issues/100>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#99 <https://github.com/tier4/ros2caret/issues/99>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore: update version to v0.4.15 (`#88 <https://github.com/tier4/ros2caret/issues/88>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#98 <https://github.com/tier4/ros2caret/issues/98>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#97 <https://github.com/tier4/ros2caret/issues/97>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#96 <https://github.com/tier4/ros2caret/issues/96>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#95 <https://github.com/tier4/ros2caret/issues/95>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump tibdex/github-app-token from 1 to 2 (`#94 <https://github.com/tier4/ros2caret/issues/94>`_)
  Bumps [tibdex/github-app-token](https://github.com/tibdex/github-app-token) from 1 to 2.
  - [Release notes](https://github.com/tibdex/github-app-token/releases)
  - [Commits](https://github.com/tibdex/github-app-token/compare/v1...v2)
  ---
  updated-dependencies:
  - dependency-name: tibdex/github-app-token
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#93 <https://github.com/tier4/ros2caret/issues/93>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#92 <https://github.com/tier4/ros2caret/issues/92>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* chore: sync files (`#91 <https://github.com/tier4/ros2caret/issues/91>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore(deps): bump actions/checkout from 3 to 4 (`#90 <https://github.com/tier4/ros2caret/issues/90>`_)
  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3...v4)
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
  ...
  Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#89 <https://github.com/tier4/ros2caret/issues/89>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.35.0 → v0.36.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.35.0...v0.36.0)
  - [github.com/pre-commit/mirrors-prettier: v3.0.2 → v3.0.3](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.2...v3.0.3)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#82 <https://github.com/tier4/ros2caret/issues/82>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.1 → v3.0.2](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.1...v3.0.2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.14 (`#83 <https://github.com/tier4/ros2caret/issues/83>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* fix: import module for annotations (`#81 <https://github.com/tier4/ros2caret/issues/81>`_)
* ci(pre-commit): autoupdate (`#80 <https://github.com/tier4/ros2caret/issues/80>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0 → v3.0.1](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0...v3.0.1)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.13 (`#79 <https://github.com/tier4/ros2caret/issues/79>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore: update version to v0.4.12 (`#77 <https://github.com/tier4/ros2caret/issues/77>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#78 <https://github.com/tier4/ros2caret/issues/78>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.9-for-vscode → v3.0.0](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.9-for-vscode...v3.0.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.11 (`#76 <https://github.com/tier4/ros2caret/issues/76>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* ci(pre-commit): autoupdate (`#73 <https://github.com/tier4/ros2caret/issues/73>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.34.0 → v0.35.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.34.0...v0.35.0)
  - [github.com/shellcheck-py/shellcheck-py: v0.9.0.2 → v0.9.0.5](https://github.com/shellcheck-py/shellcheck-py/compare/v0.9.0.2...v0.9.0.5)
  - [github.com/scop/pre-commit-shfmt: v3.6.0-2 → v3.7.0-1](https://github.com/scop/pre-commit-shfmt/compare/v3.6.0-2...v3.7.0-1)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: update version to v0.4.10.1 (`#75 <https://github.com/tier4/ros2caret/issues/75>`_)
  Co-authored-by: github-actions <github-actions@github.com>
* chore: sync files (`#74 <https://github.com/tier4/ros2caret/issues/74>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* feat: add caret version CLI (`#69 <https://github.com/tier4/ros2caret/issues/69>`_)
  * feat: added tentative version command
  * feat: added new workflow
  * feat: added new github actions
  * refactor: added some changes
  * fixed: removed pre-commit.ci error
  * fixed: removed pre-commit.ci error
  * fixed: removed pre-commit.ci error
  * fixed: removed pre-commit.ci error
  * docs: restored the contents of version.py to their original state
  * refactor: changed the contents in vrsion.py
  * fixed: removed flake8 error
  * refactor: changed version.py
  * test
  * test2
  * reverted to the first state
  * feat: creat the github actions to create PR and change version info  -s
  * feat: creat the github actions to create PR and change version info  -s
  * fixed: removed pytest erorrs
  * docs: added copyright to __version_\_.py
  * docs: yml -> yaml
  * delated update-caret-version.yml
  * fixed: pre-commit ci erorrs
  * fixed: pytest erorr
  * fixed: pytest erorr
  * fixed: pre-commit ci erorrs
  * fixed sed cmd erorr
  * fixed checkout erorr
  * fixed pre-commit erorr
  * fixed pre-commit erorr
  * fixed pre-commit erorr
  * fixed pre-commit erorr
  * fixed: changed to *
  * fixed: changed to *
  * fixed: changed script to to accurately compare version information
  * refactor: changed the way to get branch name
  * refactor: changed the way to get branch name
  * refactor: changed the way to get branch name
  * refactor: changed the way to get branch name
  * fixed: changed the dictionary's keyword in setup.py
  * fixed: added if condition to the create PR step
  * fixed: added if condition to the create PR step
  * fixed: added if condition to the create PR step
  * fixed: added if condition to the create PR step
  * fixed: added if condition to the create PR step
  * fixed: added if condition to the create PR step
  * docs: changed the PR-create step name
  * docs: added few changes
  * fixed: changed version to v0.4.10
  ---------
  Co-authored-by: taro-yu <milktea1621@gmai.com>
* Contributors: Bo Peng, ISP akm, atsushi yano, dependabot[bot], github-actions[bot], h-suzuki-isp, iwatake, pre-commit-ci[bot], system-tools-actions-public[bot], takeshi-iwanari, ymski, yu-taro-

0.4.10 (2023-06-08)
-------------------
* feat: add tracepoint for light record (`#70 <https://github.com/tier4/ros2caret/issues/70>`_)
* ci(pre-commit): autoupdate (`#71 <https://github.com/tier4/ros2caret/issues/71>`_)
  updates:
  - [github.com/adrienverge/yamllint: v1.31.0 → v1.32.0](https://github.com/adrienverge/yamllint/compare/v1.31.0...v1.32.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#68 <https://github.com/tier4/ros2caret/issues/68>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.33.0 → v0.34.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.33.0...v0.34.0)
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.6 → v3.0.0-alpha.9-for-vscode](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.6...v3.0.0-alpha.9-for-vscode)
  - [github.com/adrienverge/yamllint: v1.29.0 → v1.31.0](https://github.com/adrienverge/yamllint/compare/v1.29.0...v1.31.0)
  - [github.com/scop/pre-commit-shfmt: v3.6.0-1 → v3.6.0-2](https://github.com/scop/pre-commit-shfmt/compare/v3.6.0-1...v3.6.0-2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#67 <https://github.com/tier4/ros2caret/issues/67>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* Contributors: pre-commit-ci[bot], system-tools-actions-public[bot], takeshi-iwanari

0.4.9 (2023-03-16 11:57:45 +0900)
---------------------------------

0.4.8 (2023-03-16 11:57:45 +0900)
---------------------------------

0.4.7 (2023-03-16 11:57:45 +0900)
---------------------------------

0.4.6 (2023-03-16 11:57:45 +0900)
---------------------------------

0.4.5 (2023-03-16 11:57:45 +0900)
---------------------------------
* ci(pre-commit): autoupdate (`#66 <https://github.com/tier4/ros2caret/issues/66>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.4 → v3.0.0-alpha.6](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.4...v3.0.0-alpha.6)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#65 <https://github.com/tier4/ros2caret/issues/65>`_)
  updates:
  - [github.com/AleksaC/hadolint-py: v2.10.0 → v2.12.0.2](https://github.com/AleksaC/hadolint-py/compare/v2.10.0...v2.12.0.2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* Contributors: pre-commit-ci[bot]

0.4.4 (2023-01-19 09:48:16 +0900)
---------------------------------

0.4.3 (2023-01-19 09:48:16 +0900)
---------------------------------

0.4.2 (2023-01-19 09:48:16 +0900)
---------------------------------
* ci(pre-commit): autoupdate (`#64 <https://github.com/tier4/ros2caret/issues/64>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.32.2 → v0.33.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.32.2...v0.33.0)
  - [github.com/adrienverge/yamllint: v1.28.0 → v1.29.0](https://github.com/adrienverge/yamllint/compare/v1.28.0...v1.29.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* feat: add light mode (`#63 <https://github.com/tier4/ros2caret/issues/63>`_)
  * feat: add light mode
  * fix: add ros2_caret:caret_init
* chore: sync files (`#62 <https://github.com/tier4/ros2caret/issues/62>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* Contributors: pre-commit-ci[bot], system-tools-actions-public[bot], takeshi-iwanari

0.4.1 (2022-12-26)
------------------
* ci(pre-commit): autoupdate (`#60 <https://github.com/tier4/ros2caret/issues/60>`_)
  updates:
  - [github.com/shellcheck-py/shellcheck-py: v0.8.0.4 → v0.9.0.2](https://github.com/shellcheck-py/shellcheck-py/compare/v0.8.0.4...v0.9.0.2)
  - [github.com/scop/pre-commit-shfmt: v3.5.1-2 → v3.6.0-1](https://github.com/scop/pre-commit-shfmt/compare/v3.5.1-2...v3.6.0-1)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#61 <https://github.com/tier4/ros2caret/issues/61>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* Contributors: pre-commit-ci[bot], system-tools-actions-public[bot]

0.4.0 (2022-12-16)
------------------
* feat(record): support runtime recording (`#48 <https://github.com/tier4/ros2caret/issues/48>`_)
  * feat(record): support runtime recording
  * pass flake8
  * fix: start recording if node_num ==0
  * rename private variable names
  * modify to count-up of RECORD status
  * support -f option
  * set qos
  * support signal handler
  * rename: start.node_name to start.caret_node_name
* chore: modify pytest to humble (`#56 <https://github.com/tier4/ros2caret/issues/56>`_)
  * chore: modify pytest to humble
  * typo
  * Update .github/workflows/pytest.yaml
  Co-authored-by: Takayuki AKAMINE <38586589+takam5f2@users.noreply.github.com>
  Co-authored-by: Takayuki AKAMINE <38586589+takam5f2@users.noreply.github.com>
* Contributors: hsgwa

0.3.4 (2022-12-13)
------------------
* ci(pre-commit): autoupdate (`#59 <https://github.com/tier4/ros2caret/issues/59>`_)
  updates:
  - [github.com/scop/pre-commit-shfmt: v3.5.1-1 → v3.5.1-2](https://github.com/scop/pre-commit-shfmt/compare/v3.5.1-1...v3.5.1-2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* docs: add issue template and PR template (`#57 <https://github.com/tier4/ros2caret/issues/57>`_)
* ci(pre-commit): autoupdate (`#55 <https://github.com/tier4/ros2caret/issues/55>`_)
  updates:
  - [github.com/pre-commit/pre-commit-hooks: v4.3.0 → v4.4.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.3.0...v4.4.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* Contributors: pre-commit-ci[bot], takeshi-iwanari

0.3.3 (2022-11-28)
------------------
* fix: change standard error output of nm command (`#54 <https://github.com/tier4/ros2caret/issues/54>`_)
* fix: add some ignore file extensions into check_caret_rclcpp (`#53 <https://github.com/tier4/ros2caret/issues/53>`_)
* chore: sync files (`#52 <https://github.com/tier4/ros2caret/issues/52>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* Contributors: atsushi yano, system-tools-actions-public[bot]

0.3.2 (2022-11-14)
------------------
* chore(pytest): add no:launch_testing for caplog test in humble (`#47 <https://github.com/tier4/ros2caret/issues/47>`_)
  * chore(pytest): add no:launch_testing for caplog test in humble
  * add description in detail
  * typo
  * typo
* chore: sync files (`#51 <https://github.com/tier4/ros2caret/issues/51>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* fix: fix non-binary files to be unchecked in check_caret_rclcpp (`#44 <https://github.com/tier4/ros2caret/issues/44>`_)
  * fix: add non-binary files
  * fix: mypy error
  * fix: add non-binary files
  * style: improve readability
* chore: make force option work without argument (`#50 <https://github.com/tier4/ros2caret/issues/50>`_)
* chore: sync files (`#49 <https://github.com/tier4/ros2caret/issues/49>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#46 <https://github.com/tier4/ros2caret/issues/46>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.3 → v3.0.0-alpha.4](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.3...v3.0.0-alpha.4)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* Contributors: atsushi yano, hsgwa, pre-commit-ci[bot], system-tools-actions-public[bot]

0.3.1 (2022-10-28)
------------------
* chore: sync files (`#45 <https://github.com/tier4/ros2caret/issues/45>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#43 <https://github.com/tier4/ros2caret/issues/43>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.2 → v3.0.0-alpha.3](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.2...v3.0.0-alpha.3)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* fix(record): args error (`#42 <https://github.com/tier4/ros2caret/issues/42>`_)
* feat: add caret record CLI (`#38 <https://github.com/tier4/ros2caret/issues/38>`_)
  * feat: add caret record cli
  * typo
  * modify dict argument to tuple
* ci(pre-commit): autoupdate (`#41 <https://github.com/tier4/ros2caret/issues/41>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.1 → v3.0.0-alpha.2](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.1...v3.0.0-alpha.2)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#40 <https://github.com/tier4/ros2caret/issues/40>`_)
  updates:
  - [github.com/pre-commit/mirrors-prettier: v3.0.0-alpha.0 → v3.0.0-alpha.1](https://github.com/pre-commit/mirrors-prettier/compare/v3.0.0-alpha.0...v3.0.0-alpha.1)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#39 <https://github.com/tier4/ros2caret/issues/39>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* test: pass test in local environment (`#36 <https://github.com/tier4/ros2caret/issues/36>`_)
* chore: sync files (`#35 <https://github.com/tier4/ros2caret/issues/35>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* Contributors: hsgwa, pre-commit-ci[bot], system-tools-actions-public[bot]

0.3.0 (2022-09-15)
------------------
* ci(pre-commit): autoupdate (`#32 <https://github.com/tier4/ros2caret/issues/32>`_)
  updates:
  - [github.com/adrienverge/yamllint: v1.27.1 → v1.28.0](https://github.com/adrienverge/yamllint/compare/v1.27.1...v1.28.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: sync files (`#33 <https://github.com/tier4/ros2caret/issues/33>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore: sync files (`#28 <https://github.com/tier4/ros2caret/issues/28>`_)
  * chore: sync files
  * fix: add missing type of snippet
  Co-authored-by: takam5f2 <takam5f2@users.noreply.github.com>
  Co-authored-by: Takayuki AKAMINE <takayuki.akamine@tier4.jp>
* ci: add .cspell.json. to be synchronized (`#31 <https://github.com/tier4/ros2caret/issues/31>`_)
* docs: add notes for next development (`#30 <https://github.com/tier4/ros2caret/issues/30>`_)
  * docs: add notes for next development
  * typo
  * modify line width
  * pass flake8
* fix: lttng has no attribute last filters (`#29 <https://github.com/tier4/ros2caret/issues/29>`_)
* ci(pre-commit): autoupdate (`#27 <https://github.com/tier4/ros2caret/issues/27>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.32.1 → v0.32.2](https://github.com/igorshubovych/markdownlint-cli/compare/v0.32.1...v0.32.2)
  - [github.com/pre-commit/mirrors-prettier: v2.7.1 → v3.0.0-alpha.0](https://github.com/pre-commit/mirrors-prettier/compare/v2.7.1...v3.0.0-alpha.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#26 <https://github.com/tier4/ros2caret/issues/26>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.32.0 → v0.32.1](https://github.com/igorshubovych/markdownlint-cli/compare/v0.32.0...v0.32.1)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* feat: create and verify architecture file (`#25 <https://github.com/tier4/ros2caret/issues/25>`_)
  * feat: create architecture file
  * fix: pass flake8
  * feat: verify paths
  * fix: review comment & refactor: verify_paths
  * fix: add copyright
  * fix: address ModuleNotFoundError in github actions
  * fix: catch Exception -> (OSError, Error)
  * fix: move import caret_analyze into try block
  * fix: assign None to Error in Github actions
  * fix: review comments
  * tests: add test_verify_paths fix test_create_architecture
  * fix: pass pytest in Github Actions
* ci(pre-commit): autoupdate (`#24 <https://github.com/tier4/ros2caret/issues/24>`_)
  updates:
  - [github.com/igorshubovych/markdownlint-cli: v0.31.1 → v0.32.0](https://github.com/igorshubovych/markdownlint-cli/compare/v0.31.1...v0.32.0)
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* chore: modify test_copyright path (`#23 <https://github.com/tier4/ros2caret/issues/23>`_)
* feat: add filtering option to summary (`#20 <https://github.com/tier4/ros2caret/issues/20>`_)
  * style: pass flake8
  * feat: add filtering option to summary
  * feat: add _get_trace_creation_datatime method
  * refactor: improve readability
  * refactor: move get_measure_duration & get_trace_creation_datetime
  * fix: pass flake8
  * fix: method name
  * fix: duration -> range
  * style: improve summary appearance
  * ci(pre-commit): autofix
  * chore: fix copyright
  * chore: fix path of test_copyright & remove unnecessary comment
  * fix: change print_summary to public function & type error
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* Contributors: Takayuki AKAMINE, atsushi yano, hsgwa, pre-commit-ci[bot], system-tools-actions-public[bot]

0.2.3 (2022-07-14)
------------------
* fix: add tabulate-pip, ros2cli and delete setuptools (`#22 <https://github.com/tier4/ros2caret/issues/22>`_)
  * fix: add tabulate-pip, ros2cli and delete setuptools
  * ci(pre-commit): autofix
  * fix: change python-tabulate-pip to python3-tabulate
  Co-authored-by: Keita Miura <miura2445@mail.saitama-u.ac.jp>
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* ci(pre-commit): autoupdate (`#21 <https://github.com/tier4/ros2caret/issues/21>`_)
  * ci(pre-commit): autoupdate
  updates:
  - [github.com/pre-commit/pre-commit-hooks: v4.2.0 → v4.3.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.2.0...v4.3.0)
  - [github.com/pre-commit/mirrors-prettier: v2.6.2 → v2.7.1](https://github.com/pre-commit/mirrors-prettier/compare/v2.6.2...v2.7.1)
  - [github.com/adrienverge/yamllint: v1.26.3 → v1.27.1](https://github.com/adrienverge/yamllint/compare/v1.26.3...v1.27.1)
  - [github.com/scop/pre-commit-shfmt: v3.4.3-1 → v3.5.1-1](https://github.com/scop/pre-commit-shfmt/compare/v3.4.3-1...v3.5.1-1)
  * ci(pre-commit): autofix
  Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
* fix: check-caret-rclcpp logging output (`#19 <https://github.com/tier4/ros2caret/issues/19>`_)
  * refactor: check_caret_rclcpp
  * add: check_caret_rclcpp.py
  * add: __init_\_.py to tests dir
  * add: pytest.ini to test log
  * add: handler for for check_caret_rcll
  * add: EOF line break
  * add: copyright
  * add: python3-pytest-mock to test_depend
  * add: pytest-mock installation before pytest
  * skip mypy tests in Github action
  * rename hoge -> baz
* chore: add .pre-commit-config.yaml (`#18 <https://github.com/tier4/ros2caret/issues/18>`_)
* feat: callback uniqueness check (`#17 <https://github.com/tier4/ros2caret/issues/17>`_)
  * rm: logger handler
  * change constructor from Lttng to Architecture.
  * pass flake8
  * mod: catch exception and print its message
  * add: Lttng constructor to run lttng validate
  Co-authored-by: hsgwa <hasegawa.isp@gmail.com>
* chore: sync files (`#13 <https://github.com/tier4/ros2caret/issues/13>`_)
  Co-authored-by: keita1523 <keita1523@users.noreply.github.com>
* chore: arrange dependent packages in package.xml and requirements.txt (`#15 <https://github.com/tier4/ros2caret/issues/15>`_)
  * chore: arrange dependent packages in package.xml and requirements.txt
  * fix: resolve conflict
  * fix: delete nbformat and nbconvert
  Co-authored-by: Keita Miura <miura2445@mail.saitama-u.ac.jp>
* add nbconvert and nbformat with version (`#16 <https://github.com/tier4/ros2caret/issues/16>`_)
* Merge pull request `#12 <https://github.com/tier4/ros2caret/issues/12>`_ from hsgwa/fix_issue_11
  fix: rename tabulate dependency to rosdep compliant. closes `#11 <https://github.com/tier4/ros2caret/issues/11>`_
* rm: comment out disabled implementation
* add: copyright
* fix: flake8 err
* fix: rename tabulate dependency to rosdep compliant. closes `#11 <https://github.com/tier4/ros2caret/issues/11>`_
* Merge pull request `#7 <https://github.com/tier4/ros2caret/issues/7>`_ from tier4/dev/check_ctf_and_display_summary
  feat: CLI for batch check and summary display
* chore: add tabulate in package.xml
* Merge pull request `#9 <https://github.com/tier4/ros2caret/issues/9>`_ from tier4/sync-files
  chore: sync files
* chore: adapt GitHub actions to pytest (`#6 <https://github.com/tier4/ros2caret/issues/6>`_)
  * feat: adapt github actions to pytest
  * feat: adapt ament_mypy test
  * feat: adapt pytest with build dependency packages
  * fix: add an empty line
  * fix: delete caret_analyze_cpp_impl
* Merge pull request `#8 <https://github.com/tier4/ros2caret/issues/8>`_ from tier4/remove-gitmodules
  fix: remove .gitmodules
* chore: sync files
* fix: remove .gitmodules
* feat: CLI for batch check and summary display
* chore: sync files (`#5 <https://github.com/tier4/ros2caret/issues/5>`_)
  Co-authored-by: takam5f2 <takam5f2@users.noreply.github.com>
* fix(actions): fixed source branch
* Contributors: Takayuki AKAMINE, Tetsuo Watanabe, atsushi421, hsgwa, keita1523, pre-commit-ci[bot], system-tools-actions-public[bot], system-tools-actions[bot]

0.2.2 (2022-04-28)
------------------
* Feat/add sync file (`#4 <https://github.com/tier4/ros2caret/issues/4>`_)
  * Create sync-files.yaml
  * Create sync-files.yaml
  * Update sync-files.yaml
  * fix: sync-files.yaml
  * feat: add pytest.yaml
* tag: v0.2.1
* Contributors: hsgwa, keita1523

0.2.1 (2022-04-18)
------------------
* Merge pull request `#1 <https://github.com/tier4/ros2caret/issues/1>`_ from tier4/dev/check_caret_rclcpp
  feat: CLI to check whether caret-rclcpp is used
* style: rename directory -> workspace
* fix: variable name
* Fix: pass ament_flake8 test
* feat: CLI to check whether caret-rclcpp is used
* add: target_path_only argument
* add separate option to callback graph
* update to notebook. add node and communication
* typo
* v0.1.0
* add: package description
* support ros cli
* rename package name
* update to notebook. add node and communication
* add: record sort
* add __str_\_ interface to path class
* support yaml path_alias
* modify lost case for merge_sequencial
* disable cursor  control
* modify to avoid keyerr exception
* remove debug print
* fix record merge bug. and change algorithm to O(N)
* add json export and import iterface for debugging
* typo
* change merge_sequencial algorithm. O(N) version.
* is_cpp_impl_valid and clean tests
* typo
* add default argument to progress_label
* fix copy constructor
* fix records rclcpp copy constructor
* add progress to cpp impl
* fix: copy constructor
* fix assertions when there are zero records.
* Change the records calculation to later and cash it.
* Modify test requirements
* Fixed to automatically switch between C++ and Python implementations.
* modify timestamp time to uint64_t
* change record impl from py to cpp
* add cpp records impl
* move merge impl to records
* change record an records interface
* clean: divide pybind and impl files
* add: pybind11 sample code
* add: __init_\_.py for test dir
* move python scripts to sub-directory
* fix: callback object keyerror
* modify tracepoint: merge source_timestamp to dispatch_subscription_callback
* fix: wrong column when message is lost.
* Fix: to_histogram bug and modify lttng interface.
* Change all merges to left join to detect lost in the middle.
* Fixed behavior when all messages are lost, added error messages.
* Fixed a bug where a column disappears in the middle.
* clean
* Fixed typing type definition.
* Change the way DataFrame columns are sorted.
* remove unnecessary call: pd.dropna
* modify test_path_latency
* modify merge_sequencial process and api
* modify ytick labels
* add notebook samples
* fix: remove_dropped
* move lttng_samples to sample dir
* add: related scripts
* add: architecture.yaml for sample ctf files
* add: sample ctf files
* add: record.py and test_record.py
* add: initial files
* add: LICENSE
* add: CONTRIBUTING.md
* first commit
* Contributors: atsushi421, hsgwa
