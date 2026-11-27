# Master's Thesis Research Library — student environment

**Private technical rehearsal; no thesis is available for assignment or publication yet.** This repository is separate from the supervisor's master. It contains only generic environment tools and a neutral demonstration notebook. There is deliberately no site/ directory, release manifest, thesis source, private pilot, provider data, or active Pages workflow.

## First use (no terminal commands and no forwarded port needed)

1. Open a new Codespace from [this repository's main branch](https://codespaces.new/robertomarfe/thesis-catalogue-students/tree/main). Check the account's Codespaces cost/usage indication before creating it. The Python 3.13 devcontainer automatically creates a new .venv, installs the five exact direct pins, runs pip check, executes a neutral notebook in the exact environment and tests token-protected JupyterLab on loopback. A successful setup prints RUNTIME VERIFIED.
2. To see the receipt, press Ctrl+Shift+P, choose Tasks: Run Task, then **Mostra esito installazione Python**. A genuine fresh successful installation reports fresh_install_this_run: true, isolated_no_system_packages: true, pip_check: pass, notebook executed: true, and JupyterLab API 403 without authentication / 200 with authentication. The receipt is local and does not contain tokens. If setup failed, send the error text with credentials redacted; do not make a port public or change package pins. If no environment was created, the other graphical task **Prepara e verifica ambiente Python** runs setup. Rechecking an existing environment is not evidence of a fresh installation.

Optional: open demo/runtime_check.ipynb and choose the .venv Python kernel, then Run All. It should end with RUNTIME_CHECK_PASS. This exercise solves only a generic linear system and checks a synthetic random sample; it is not a research solution. Don't commit executed outputs. Stop the Codespace when finished to avoid unnecessary usage.

## Publication boundary

The independent release verifier and runtime are included for future authorized releases. They cannot prepare a thesis without a sealed student site and selected ID. The Pages workflow is an inactive example under deployment/, not a configured workflow. Do not activate it or publish this rehearsal. Approved research materials will be prepared by the separate source-bound staging process after explicit authorization. Do not copy the supervisor's master, private audit or provider data here.

The local environment probe passed with the already-installed pinned Python 3.13.5 environment and a nonprivileged user. Actual clean package installation, devcontainer provisioning and forwarded/browser JupyterLab access are still to be verified. Direct pins are not a complete transitive lock; the local receipt records the actual installed versions after successful checks.
