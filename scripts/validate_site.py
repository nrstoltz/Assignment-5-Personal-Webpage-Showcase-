#!/usr/bin/env python3
"""
Simple site validation for the TEMPLATE folder.
Checks:
 - lists HTML files
 - parses each HTML file for <img> alt attributes
 - checks local <a href> targets exist (ignores http/mailto/#)
 - checks linked CSS files exist
 - ensures main navigation contains expected pages
 - prints git status summary
"""
import os
from html.parser import HTMLParser
import subprocess

ROOT = os.path.dirname(os.path.dirname(__file__))
EXPECTED_NAV = {'index.html','about.html','resume.html','projects.html','contact.html'}

class QuickParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs = []
        self.hrefs = []
        self.css = []
        self.text = ''
        self.in_nav = False
        self.nav_hrefs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            self.imgs.append((attrs.get('src'), attrs.get('alt')))
        if tag == 'a':
            href = attrs.get('href')
            if href:
                self.hrefs.append(href)
                if self.in_nav:
                    self.nav_hrefs.append(href)
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.css.append(attrs.get('href'))
        if tag == 'nav':
            self.in_nav = True
    def handle_data(self, data):
        self.text += data
    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False


def find_html_files(root):
    return sorted([f for f in os.listdir(root) if f.endswith('.html')])


def check_file(path):
    issues = []
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    p = QuickParser()
    try:
        p.feed(data)
    except Exception as e:
        issues.append(('parse-error', str(e)))
        return issues, p
    # imgs
    for src, alt in p.imgs:
        if src and (alt is None or alt.strip() == ''):
            issues.append(('img-missing-alt', src))
    # css
    for css in p.css:
        if css and not os.path.exists(os.path.join(ROOT, css)):
            issues.append(('missing-css', css))
    # hrefs
    for href in p.hrefs:
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('#'):
            continue
        cleaned = href.split('?')[0].split('#')[0]
        target = os.path.join(ROOT, cleaned)
        if not os.path.exists(target):
            issues.append(('broken-link', href))
    return issues, p


def basic_css_check(css_path):
    """Return list of issues for this css file (very basic: balanced braces)."""
    issues = []
    full = os.path.join(ROOT, css_path)
    if not os.path.exists(full):
        issues.append(('missing-css', css_path))
        return issues
    try:
        with open(full, 'r', encoding='utf-8') as f:
            data = f.read()
    except Exception as e:
        issues.append(('css-read-error', css_path, str(e)))
        return issues
    # check braces roughly
    open_braces = data.count('{')
    close_braces = data.count('}')
    if open_braces != close_braces:
        issues.append(('css-unbalanced-braces', css_path, open_braces, close_braces))
    return issues


def git_clean(root):
    try:
        out = subprocess.check_output(['git','status','--porcelain'], cwd=root, text=True)
        return out.strip() == '', out
    except Exception as e:
        return None, str(e)


def main():
    print('Root:', ROOT)
    html_files = find_html_files(ROOT)
    if not html_files:
        print('No HTML files found in', ROOT)
        return
    print('HTML files found:', html_files)
    overall_issues = {}
    for hf in html_files:
        path = os.path.join(ROOT, hf)
        print('\nChecking', hf)
        issues, parser = check_file(path)
        if not issues:
            print('  OK')
        else:
            for it in issues:
                print('  ISSUE:', it)
            overall_issues[hf] = issues
        # check nav presence by examining hrefs found inside <nav>
        found = set()
        for h in parser.nav_hrefs:
            cleaned = h.split('?')[0].split('#')[0]
            # normalize to filename if path-like
            found.add(os.path.basename(cleaned))
        missing = EXPECTED_NAV - found
        nav_ok = len(missing) == 0
        print('  Navigation contains expected main links?', 'YES' if nav_ok else 'NO')
        if not nav_ok:
            print('   Missing nav links:', sorted(missing))
    clean, out = git_clean(ROOT)
    if clean is None:
        print('\nCould not check git status:', out)
    else:
        print('\nGit working tree clean?', 'YES' if clean else 'NO')
        if not clean:
            print(out)
    print('\nSummary:')
    if not overall_issues:
        print('No issues found by quick validator.')
    else:
        for hf, issues in overall_issues.items():
            print(hf, '->', issues)

if __name__ == '__main__':
    main()
