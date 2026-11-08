"""Live inventory of every skill installed on this machine, with where it came from and what it does.

Used by /improve-project (phase 2: pick skills from what is really installed) and by skill-scout
(keeps the skills site's "installed" section true).

Usage:
  python -I inventory.py                 # markdown table to stdout
  python -I inventory.py --json out.json # JSON list
  python -I inventory.py --project <dir> # also include <dir>/.claude/skills (default: current dir)

Groups:
  own      ~/.claude/skills (installed with `npx skills` or by hand, incl. Dor's own skills)
  project  <project>/.claude/skills (only in that project)
  plugin   plugins installed with `claude plugin install` (installed_plugins.json)
  account  skills and plugins that come with Dor's Claude account (synced folders)
"""
import json, os, re, sys, glob

HOME = os.path.expanduser("~")
CL = os.path.join(HOME, ".claude")


def front(path):
    """name + description from a SKILL.md / command .md front matter."""
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read(6000)
    except OSError:
        return None, ""
    m = re.match(r"---\s*\n(.*?)\n---", txt, re.S)
    head = m.group(1) if m else ""
    name = re.search(r"^name:\s*(.+)$", head, re.M)
    desc = re.search(r"^description:\s*(.+?)(?=\n[A-Za-z_-]+:|\Z)", head, re.S | re.M)
    d = re.sub(r"\s+", " ", desc.group(1)).strip().strip("'\"").lstrip(">|- ").strip() if desc else ""
    return (name.group(1).strip().strip("'\"") if name else None), d[:260]


def skills_in(folder):
    out = []
    for p in sorted(glob.glob(os.path.join(folder, "*", "SKILL.md"))):
        n, d = front(p)
        out.append((n or os.path.basename(os.path.dirname(p)), d, os.path.dirname(p)))
    return out


def lock_sources():
    src = {}
    try:
        d = json.load(open(os.path.join(HOME, ".agents", ".skill-lock.json"), encoding="utf-8"))
        for k, v in (d.get("skills") or {}).items():
            src[k] = v.get("source") or v.get("sourceUrl") or ""
    except Exception:
        pass
    return src


def main():
    args = sys.argv[1:]
    proj = os.getcwd()
    if "--project" in args:
        proj = args[args.index("--project") + 1]
    rows = []
    src = lock_sources()

    # own skills
    for n, d, path in skills_in(os.path.join(CL, "skills")):
        if os.path.basename(path) == "synced":
            continue
        rows.append({"group": "own", "call": "/" + n, "name": n, "package": "", "source": src.get(n, ""), "desc": d, "path": path})

    # project skills
    pdir = os.path.join(proj, ".claude", "skills")
    if os.path.isdir(pdir):
        for n, d, path in skills_in(pdir):
            if not os.path.exists(os.path.join(path, "SKILL.md")):
                continue
            rows.append({"group": "project", "call": "/" + n, "name": n, "package": os.path.basename(proj), "source": "", "desc": d, "path": path})

    # installed plugins
    try:
        ip = json.load(open(os.path.join(CL, "plugins", "installed_plugins.json"), encoding="utf-8"))
        for key, inst in (ip.get("plugins") or ip).items():
            inst = inst[0] if isinstance(inst, list) else inst
            base = inst.get("installPath", "")
            plug, market = key.split("@", 1) if "@" in key else (key, "")
            found = glob.glob(os.path.join(base, "**", "SKILL.md"), recursive=True, include_hidden=True)
            found += glob.glob(os.path.join(base, "commands", "*.md"))
            for p in sorted(set(found)):
                n, d = front(p)
                n = n or (os.path.basename(os.path.dirname(p)) if p.endswith("SKILL.md") else os.path.splitext(os.path.basename(p))[0])
                rows.append({"group": "plugin", "call": f"/{plug}:{n}", "name": n, "package": plug, "source": market, "desc": d, "path": os.path.dirname(p)})
    except Exception as e:
        print("warn: plugins:", e, file=sys.stderr)

    # account (synced) plugins and skills
    for root in glob.glob(os.path.join(CL, "plugins", "synced", "*")):
        for pdir in sorted(glob.glob(os.path.join(root, "*"))):
            if not os.path.isdir(pdir):
                continue
            pj = glob.glob(os.path.join(pdir, "**", "plugin.json"), recursive=True, include_hidden=True)
            plug = os.path.basename(pdir)
            if pj:
                try:
                    plug = json.load(open(pj[0], encoding="utf-8")).get("name", plug)
                except Exception:
                    pass
            for p in sorted(glob.glob(os.path.join(pdir, "**", "SKILL.md"), recursive=True)):
                n, d = front(p)
                n = n or os.path.basename(os.path.dirname(p))
                rows.append({"group": "account", "call": f"/{plug}:{n}", "name": n, "package": plug, "source": "Claude account", "desc": d, "path": os.path.dirname(p)})
    for root in glob.glob(os.path.join(CL, "skills", "synced", "*")):
        for n, d, path in skills_in(root):
            rows.append({"group": "account", "call": f"/anthropic-skills:{n}", "name": n, "package": "anthropic-skills", "source": "Claude account", "desc": d, "path": path})

    # de-duplicate (same call)
    seen, uniq = set(), []
    for r in rows:
        if r["call"] in seen:
            continue
        seen.add(r["call"]); uniq.append(r)

    if "--json" in args:
        out = args[args.index("--json") + 1]
        json.dump(uniq, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"{len(uniq)} skills -> {out}")
        return
    counts = {}
    for r in uniq:
        counts[r["group"]] = counts.get(r["group"], 0) + 1
    print(f"# Installed skills: {len(uniq)} ({', '.join(f'{k} {v}' for k, v in counts.items())})\n")
    print("| group | call | package | what it does |\n|---|---|---|---|")
    for r in uniq:
        print(f"| {r['group']} | `{r['call']}` | {r['package']} | {r['desc'][:160].replace('|', '/')} |")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
