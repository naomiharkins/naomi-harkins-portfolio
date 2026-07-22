# Publish This Portfolio to GitHub and GitHub Pages

The easiest method does not require Terminal.

## Before you begin

- Use Naomi's GitHub account so the portfolio ownership and commit history match the applicant.
- Extract the ZIP file first. Do **not** upload the ZIP itself.
- Open the extracted `naomi-harkins-portfolio` folder.
- Upload the contents inside that folder so `index.html`, `styles.css`, `assets`, `projects`, and `resume` appear at the top level of the repository.

## Method 1: Upload through the GitHub website

### 1. Create the repository

1. Sign in to GitHub.
2. Select the **+** menu in the upper-right corner and choose **New repository**.
3. Recommended repository name: `naomi-harkins-portfolio`.
4. Add a description such as: `Quality assurance, scientific data, and analytics portfolio for Naomi Harkins.`
5. Choose **Public** so recruiters can view it without signing in.
6. Leave the repository uninitialized if GitHub gives you the option; the portfolio already contains a README.
7. Select **Create repository**.

### 2. Upload the site files

1. On the empty repository page, choose **uploading an existing file**. On an initialized repository, choose **Add file → Upload files**.
2. Drag the contents of the extracted portfolio folder into the upload area. Upload folders and files, not the ZIP archive.
3. Confirm that `index.html` will appear in the repository root rather than inside another nested folder.
4. Use the commit message `Publish Naomi Harkins portfolio`.
5. Commit the files to the `main` branch.

### 3. Turn on GitHub Pages

1. Open the repository's **Settings** tab.
2. In the left sidebar, open **Pages** under **Code and automation**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Select the `main` branch and the `/(root)` folder.
5. Select **Save**.
6. Wait for the deployment to finish. GitHub may take several minutes to publish the first version.
7. Return to **Settings → Pages** and select **Visit site** when it appears.

For a repository named `naomi-harkins-portfolio`, the normal project-site address is:

```text
https://YOUR-USERNAME.github.io/naomi-harkins-portfolio/
```

## Cleaner URL option

A personal GitHub Pages site can use the root address:

```text
https://YOUR-USERNAME.github.io/
```

To use that format, create the repository with the exact name `YOUR-USERNAME.github.io` instead. GitHub allows one user or organization site per account.

## Method 2: Upload with Terminal

Create an empty public repository first, then run these commands from the extracted portfolio folder. Replace `YOUR-USERNAME` with Naomi's GitHub username.

```bash
cd /path/to/naomi-harkins-portfolio
git init
git add .
git commit -m "Publish Naomi Harkins portfolio"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/naomi-harkins-portfolio.git
git push -u origin main
```

Then enable GitHub Pages using **Settings → Pages → Deploy from a branch → main → /(root)**.

## Test the published site

Open the live Pages URL and check:

- Home, Projects, Skills, and Resume navigation
- All five project cards
- All project-file links
- PDF and Word resume links
- Email link
- Mobile layout and keyboard focus

If the homepage returns a 404, confirm that `index.html` is at the repository root and that Pages is publishing from `main` and `/(root)`.

## Share the portfolio

Share the live GitHub Pages URL, not a local file path and not the ZIP file. Good locations include:

- Resume contact line
- LinkedIn **Featured** section
- GitHub profile bio or pinned repository
- Job application website/portfolio field
- Cover letter signature

The repository URL is also useful when a recruiter wants to inspect the project files:

```text
https://github.com/YOUR-USERNAME/naomi-harkins-portfolio
```

## Update the site later

To update through the browser, open the repository, choose **Add file → Upload files**, upload the changed files with the same paths, and commit. GitHub Pages will redeploy automatically after the branch changes.

To update through Terminal:

```bash
git add .
git commit -m "Update portfolio"
git push
```
