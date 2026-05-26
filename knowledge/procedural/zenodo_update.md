# Procedural Guide: Updating the Zenodo Archive and DOI Record

This guide outlines the step-by-step workflow to update the repository's Zenodo archival record and mint new versioned DOIs when pushing updates to the public repository.

## Overview

Zenodo connects to the GitHub repository via a webhook. This integration is designed so that Zenodo **automatically archives a new version only when a new GitHub Release is created**. Simply pushing commits to the `main` branch (`git push`) does *not* trigger a new version on Zenodo.

---

## Step-by-Step Release & Update Workflow

Follow these steps to push updates and automatically sync them to Zenodo.

### Step 1: Push Commits to GitHub
Ensure all your local changes are committed and pushed to the public remote repository:
```bash
git push public main
```

### Step 2: Create a New Git Tag
Create a new version tag locally. Use standard semantic versioning (e.g., incrementing the patch version from `v1.0.0` to `v1.0.1`):
```bash
git tag -a v1.0.1 -m "docs: surgically excise entire oilfield domain to establish absolute corporate shield"
```

### Step 3: Push the Tag to GitHub
Push the newly created tag to the public remote repository:
```bash
git push public v1.0.1
```

### Step 4: Publish a GitHub Release
To trigger the Zenodo archive webhook, you must draft and publish a GitHub Release matching the tag:
1. Open the repository on GitHub: `https://github.com/globe-and-atlas/remote-sensing-research`.
2. On the right-hand sidebar, click on **Releases** $\rightarrow$ **Draft a new release**.
3. Under **Choose a tag**, select the tag you just pushed (`v1.0.1`).
4. Set the **Release title** (e.g., `v1.0.1: Clean Global Spectral Index Atlas Release`).
5. Add a brief summary of the changes in the release notes box (e.g., "Surgically excise oilfield domain to establish absolute corporate IP shield").
6. Click **Publish release**.

*(Alternative using the GitHub CLI)*:
If you have the `gh` command-line tool installed, you can create and publish the release directly from the terminal:
```bash
gh release create v1.0.1 --title "v1.0.1: Clean Global Spectral Index Atlas Release" --notes "Surgically excise oilfield domain"
```

### Step 5: Automatic Zenodo Processing
Once the release is published on GitHub, Zenodo receives the webhook:
* Within 1–2 minutes, Zenodo will clone the repository, package the release files as a `.zip`, and assign it a version-specific DOI.
* Go to your dashboard at [zenodo.org](https://zenodo.org/) under **My uploads** to monitor the progress.

---

## Concept DOIs vs. Version DOIs

Zenodo mints two types of DOIs for every repository:
1.  **Concept DOI**: A persistent identifier that represents the *entire* software project across all of its versions.
2.  **Version DOI**: A unique identifier tied strictly to a *specific* release (e.g., one for `v1.0.0` and a new one for `v1.0.1`).

> [!IMPORTANT]
> **No Badge Updates Needed!**
> The Zenodo badge in the public [README.md](../../README.md) is configured to use the **Concept DOI** (`10.5281/zenodo.20400744`). Since the Concept DOI automatically routes users to the *latest* versioned release, **you do not need to edit or change the DOI badge in the README or manuscript files when publishing new versions**. It stays valid forever.

---

## Manual Metadata Updates

If you need to change metadata (e.g., editing authors, description, keywords, or license) *without* modifying the repository files:
1. Log into your account on [zenodo.org](https://zenodo.org/).
2. Go to **My uploads** in the header.
3. Click on the remote-sensing-research record.
4. Click the **Edit** button in the top right.
5. Make your modifications to the fields and click **Save**.
6. Click **Publish** to make the metadata edits public.
